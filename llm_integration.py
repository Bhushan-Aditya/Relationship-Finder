from typing import List, Dict

try:
    from transformers import pipeline
    pipe = pipeline("text2text-generation", model="t5-small")
except Exception:
    pipe = None

def extract_with_llm(text: str) -> List[Dict]:
    """
    Use a T5 model to extract relationships from text.
    Returns a list of relationship dicts: {'from': ..., 'to': ..., 'relation': ..., 'confidence': ...}
    """
    if pipe is None:
        return []
    try:
        prompt = f"Extract family relationships as triples: {text}"
        result = pipe(prompt, max_new_tokens=64)[0]['generated_text']
        # Example output: "K J brother; J N sister"
        triples = []
        for part in result.split(';'):
            tokens = part.strip().split()
            if len(tokens) == 3:
                triples.append({'from': tokens[0], 'to': tokens[1], 'relation': tokens[2], 'confidence': 0.9})
        return triples
    except Exception as e:
        # If transformers/torch not installed or error, fallback to empty
        return [] 