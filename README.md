# Family Relationship Reasoning API

A robust backend for analyzing and answering complex family relationship queries from natural language, using a hybrid of dependency parsing, rule-based logic, and symbolic inference. Designed for extensibility with LLM integration.

## Features
- Extracts entities and relationships from natural language (e.g., "A is B's brother")
- Handles nested and composite relationships
- Symbolic logic for multi-step inference (e.g., "A is C's uncle" via B)
- FastAPI backend with a single `/analyze` endpoint
- spaCy for dependency parsing
- Rule-based extraction for common patterns
- Placeholder for LLM integration (e.g., T5, LLaMA)

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage
Run the API:
```bash
uvicorn main:app --reload
```

POST to `/analyze`:
```json
{
  "text": "K is J's brother. J is N's sister.",
  "question": "how is K related to N"
}
```

Response:
```json
{
  "nodes": [...],
  "edges": [...],
  "metadata": {...},
  "answer": "K is N's brother"
}
```

## Extending
- Add new rules in `relation_extractor.py`
- Add symbolic logic in `logic_layer.py`
- Integrate LLMs in `llm_integration.py` 