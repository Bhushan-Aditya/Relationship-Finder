import spacy

def resolve_coref(text: str) -> str:
    try:
        import neuralcoref
        nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(nlp)
        doc = nlp(text)
        return doc._.coref_resolved
    except Exception:
        return text 