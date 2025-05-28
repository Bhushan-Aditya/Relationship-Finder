from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from relation_extractor import RelationExtractor
from logic_layer import infer_indirect_relationships
from llm_integration import extract_with_llm
from gemini_extraction import extract_with_gemini
from gender_utils import get_gender
from coref_utils import resolve_coref
import logging
import json
import traceback

app = FastAPI(title="Family Relationship Reasoning API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

class AnalyzeRequest(BaseModel):
    text: str
    question: Optional[str] = None

class AnalyzeResponse(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    answer: Optional[str] = None
    reasoning: Optional[List[str]] = None
    confidence: Optional[float] = None
    all_answers: Optional[List[Dict[str, Any]]] = None

class FeedbackRequest(BaseModel):
    text: str
    question: str
    correct_answer: str
    notes: Optional[str] = None

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        # 0. Co-reference resolution
        resolved_text = resolve_coref(request.text)
        # 1. Gemini extraction first
        gemini_relationships = extract_with_gemini(resolved_text)
        # 2. LLM extraction (T5) fallback
        llm_relationships = extract_with_llm(resolved_text) if not gemini_relationships else []
        # 3. Rule-based fallback
        relationships = (
            gemini_relationships or
            llm_relationships or
            RelationExtractor().extract_relations(resolved_text)
        )
        # 4. Gender inference for each entity
        entities = set()
        for rel in relationships:
            try:
                if not all(k in rel for k in ("from", "to")):
                    print(f"[DEBUG] Skipping malformed relationship (entities): {rel}")
                    continue
                entities.add(rel['from'])
                entities.add(rel['to'])
            except Exception as e:
                print(f"[DEBUG] Exception in entity extraction: {e}, rel={rel}")
                continue
        gender_map = {e: get_gender(e) for e in entities}
        # 5. Symbolic inference for indirect relationships
        indirect = infer_indirect_relationships(relationships)
        all_relationships = relationships + indirect

        # Sanitize all relationships before further processing
        def is_valid_rel(rel):
            return (
                isinstance(rel, dict)
                and all(isinstance(rel.get(k), str) for k in ("from", "to", "relation"))
            )

        sanitized_relationships = []
        for rel in all_relationships:
            try:
                # Normalize keys: remove extra quotes, whitespace, lowercase
                def norm(k):
                    if isinstance(k, str):
                        k = k.strip()
                        if k.startswith('"') and k.endswith('"'):
                            k = k[1:-1]
                        k = k.strip().lower()
                    return k
                rel_norm = {norm(k): v for k, v in rel.items()}
                if is_valid_rel(rel_norm):
                    sanitized_relationships.append(rel_norm)
                else:
                    print(f"[DEBUG] Skipping unsanitized relationship: {rel}")
            except Exception as e:
                print(f"[DEBUG] Exception in relationship sanitization: {e}, rel={rel}")
        all_relationships = sanitized_relationships
        relationships = [r for r in relationships if r in all_relationships]
        indirect = [r for r in indirect if r in all_relationships]
        # 6. Build nodes and edges
        nodes = [
            {"id": f"e_{i}", "text": ent, "type": "PERSON", "gender": gender_map[ent], "position": {"x": 0, "y": 0}}
            for i, ent in enumerate(sorted(entities))
        ]
        edges = []
        for rel in all_relationships:
            try:
                if not all(k in rel for k in ("from", "to", "relation")):
                    print(f"[DEBUG] Skipping malformed relationship (edges): {rel}")
                    continue
                from_id = next(n["id"] for n in nodes if n["text"] == rel['from'])
                to_id = next(n["id"] for n in nodes if n["text"] == rel['to'])
                edge = {
                    "source": from_id,
                    "target": to_id,
                    "type": "family",
                    "text": rel['relation'],
                    "confidence": rel.get('confidence', 1.0)
                }
                edges.append(edge)
            except Exception as e:
                print(f"[DEBUG] Exception in edge extraction: {e}, rel={rel}")
                continue
        # 7. Answer the question if present
        answer = None
        reasoning = []
        confidence = None
        all_answers = []
        if request.question:
            import re
            match = re.search(r'how is (\w+) related to (\w+)', request.question, re.IGNORECASE)
            if match:
                person1, person2 = match.groups()
                found = []
                for rel in all_relationships:
                    try:
                        if not all(k in rel for k in ("from", "to", "relation")):
                            print(f"[DEBUG] Skipping malformed relationship (qa): {rel}")
                            continue
                        if (
                            (rel['from'].lower() == person1.lower() and rel['to'].lower() == person2.lower()) or
                            (rel['from'].lower() == person2.lower() and rel['to'].lower() and rel['relation'] in {"cousin", "sibling", "brother", "sister"})
                        ):
                            found.append(rel)
                    except Exception as e:
                        print(f"[DEBUG] Exception in QA extraction: {e}, rel={rel}")
                        continue
                if found:
                    for rel in found:
                        try:
                            if rel['from'].lower() == person1.lower():
                                ans = f"{person1} is {person2}'s {rel['relation']}"
                            else:
                                ans = f"{person1} is {person2}'s {rel['relation']}"
                            all_answers.append({
                                "answer": ans,
                                "confidence": rel.get('confidence', 1.0),
                                "reasoning": rel.get('via', None)
                            })
                            if 'via' in rel and rel['via']:
                                if isinstance(rel['via'], (list, tuple)):
                                    path = f"Path: {person1} -> " + " -> ".join(str(x) for x in rel['via']) + f" -> {person2}"
                                else:
                                    path = f"Path: {person1} -> {rel['via']} -> {person2}"
                                reasoning.append(f"{ans} ({path})")
                            else:
                                reasoning.append(ans)
                        except Exception as e:
                            print(f"[DEBUG] Exception in QA answer formatting: {e}, rel={rel}")
                            continue
                    best = max(all_answers, key=lambda x: x['confidence'])
                    answer = best['answer']
                    confidence = best['confidence']
                else:
                    answer = f"No direct or indirect relationship found between {person1} and {person2}"
                    reasoning.append(answer)
            else:
                answer = "Could not parse the question."
                reasoning.append(answer)
        for r in reasoning:
            logging.info(f"REASONING: {r}")
        return AnalyzeResponse(
            nodes=nodes,
            edges=edges,
            metadata={
                "total_entities": len(nodes),
                "total_relations": len(edges),
                "entity_types": ["PERSON"],
                "relation_types": ["family"]
            },
            answer=answer,
            reasoning=reasoning,
            confidence=confidence,
            all_answers=all_answers
        )
    except Exception as e:
        print("[DEBUG] Exception in /analyze:", type(e), e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback")
async def feedback(data: FeedbackRequest):
    # Store feedback in a JSONL file for active learning
    with open("feedback.jsonl", "a") as f:
        f.write(json.dumps(data.dict()) + "\n")
    logging.info(f"FEEDBACK: {data.dict()}")
    return {"status": "received"}

@app.get("/graph")
async def get_graph(text: str):
    resolved_text = resolve_coref(text)
    gemini_relationships = extract_with_gemini(resolved_text)
    llm_relationships = extract_with_llm(resolved_text) if not gemini_relationships else []
    relationships = (
        gemini_relationships or
        llm_relationships or
        RelationExtractor().extract_relations(resolved_text)
    )
    indirect = infer_indirect_relationships(relationships)
    all_relationships = relationships + indirect
    return {"relationships": all_relationships}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 