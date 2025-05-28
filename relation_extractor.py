from typing import List, Dict, Tuple, Any
import spacy
import re

class RelationExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.family_terms = [
            "brother", "sister", "father", "mother", "son", "daughter", "husband", "wife",
            "uncle", "aunt", "grandfather", "grandmother", "grandson", "granddaughter",
            "cousin", "nephew", "niece", "parent", "child", "in-law", "stepfather", "stepmother",
            "stepson", "stepdaughter", "stepbrother", "stepsister"
        ]

    def extract_relations(self, text: str) -> List[Dict]:
        doc = self.nlp(text)
        relationships = []
        sentences = [s.text.strip() for s in doc.sents]
        for sentence in sentences:
            # Pattern 1: "X is Y's Z"
            match = re.search(r"([\w']+) is ([\w']+)'s ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, person2, relation = match.groups()
                relationships.append({'from': person1, 'to': person2, 'relation': relation.lower(), 'pattern': "X is Y's Z"})
                continue
            # Pattern 2: "X is Z of Y"
            match = re.search(r"([\w']+) is ([\w']+) of ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, relation, person2 = match.groups()
                relationships.append({'from': person1, 'to': person2, 'relation': relation.lower(), 'pattern': "X is Z of Y"})
                continue
            # Pattern 3: "X is Y Z"
            match = re.search(r"([\w']+) is ([\w']+) ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, person2, relation = match.groups()
                relationships.append({'from': person1, 'to': person2, 'relation': relation.lower(), 'pattern': "X is Y Z"})
                continue
            # Pattern 4: "X and Y are siblings" or "X and Y are brothers/sisters"
            match = re.search(r"([\w']+) and ([\w']+) are ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, person2, relation = match.groups()
                rel = relation.lower().rstrip('s')
                relationships.append({'from': person1, 'to': person2, 'relation': rel, 'pattern': "X and Y are Z"})
                relationships.append({'from': person2, 'to': person1, 'relation': rel, 'pattern': "X and Y are Z"})
                continue
            # Pattern 5: "X, the father of Y" or "X, Y's uncle"
            match = re.search(r"([\w']+), the ([\w']+) of ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, relation, person2 = match.groups()
                relationships.append({'from': person1, 'to': person2, 'relation': relation.lower(), 'pattern': "X, the Z of Y"})
                continue
            match = re.search(r"([\w']+), ([\w']+)'s ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, person2, relation = match.groups()
                relationships.append({'from': person1, 'to': person2, 'relation': relation.lower(), 'pattern': "X, Y's Z"})
                continue
            # Pattern 6: "Y's uncle X" (possessive first)
            match = re.search(r"([\w']+)'s ([\w']+) ([\w']+)", sentence, re.IGNORECASE)
            if match:
                person1, relation, person2 = match.groups()
                relationships.append({'from': person2, 'to': person1, 'relation': relation.lower(), 'pattern': "Y's Z X"})
                continue
            # Pattern 7: Dependency parsing fallback for family terms
            for token in doc:
                if token.lemma_.lower() in self.family_terms:
                    subj = [w for w in token.head.lefts if w.dep_ == "nsubj"]
                    poss = [w for w in token.lefts if w.dep_ == "poss"]
                    if subj and poss:
                        relationships.append({'from': subj[0].text, 'to': poss[0].text, 'relation': token.lemma_.lower(), 'pattern': "dep_fallback"})
        return relationships

    def _find_subject(self, token) -> Any:
        """Find the subject of a verb."""
        for child in token.head.children:
            if child.dep_ in ["nsubj", "nsubjpass"]:
                return child
        return None

    def _find_object(self, token) -> Any:
        """Find the object of a verb."""
        for child in token.head.children:
            if child.dep_ in ["dobj", "pobj"]:
                return child
        return None

    def _determine_relation_type(self, verb: str) -> str:
        """Determine the type of relation based on the verb."""
        for rel_type, patterns in self.relation_patterns.items():
            if any(pattern in verb for pattern in patterns):
                return rel_type
        return "association"  # Default relation type

    def _find_entity_id(self, entities: List[Dict[str, Any]], text: str) -> str:
        """Find the entity ID that matches the given text."""
        for entity in entities:
            if entity["text"].lower() == text.lower():
                return entity["id"]
        return None

    def _find_or_add_entity(self, entities: List[Dict[str, Any]], entity_texts: set, text: str) -> str:
        for entity in entities:
            if entity["text"].lower() == text.lower():
                return entity["id"]
        new_id = f"e_{len(entities)}"
        entities.append({
            "id": new_id,
            "text": text,
            "type": "PROPN",
            "start": -1,
            "end": -1
        })
        entity_texts.add(text.lower())
        return new_id 