import networkx as nx
from typing import List, Dict

def infer_indirect_relationships(relationships: List[Dict]) -> List[Dict]:
    """Infer indirect relationships (uncle, aunt, cousin, niece/nephew, in-law, step, grandparent, sibling, etc.) using a graph."""
    G = nx.DiGraph()
    gender_map = {}
    for rel in relationships:
        G.add_edge(rel['from'], rel['to'], relation=rel['relation'])
        # Track gender for in-law and parent/child
        if rel['relation'] in ('father', 'son', 'brother', 'husband', 'grandfather', 'uncle', 'nephew', 'grandson'):
            gender_map[rel['from']] = 'male'
        if rel['relation'] in ('mother', 'daughter', 'sister', 'wife', 'grandmother', 'aunt', 'niece', 'granddaughter'):
            gender_map[rel['from']] = 'female'
    indirect = []
    # Transitive sibling: if A is B's sibling and B is C's sibling, then A is C's sibling
    for a in G.nodes:
        for b in G.successors(a):
            rel1 = G[a][b]['relation']
            if rel1 in ('brother', 'sister', 'sibling'):
                for c in G.successors(b):
                    rel2 = G[b][c]['relation']
                    if rel2 in ('brother', 'sister', 'sibling') and a != c:
                        # Infer sibling
                        if not G.has_edge(a, c):
                            sib_type = 'brother' if gender_map.get(a) == 'male' else 'sister' if gender_map.get(a) == 'female' else 'sibling'
                            indirect.append({'from': a, 'to': c, 'relation': sib_type, 'via': b})
    # Multi-hop uncle/aunt: any path from A to D with one or more sibling links then a parent link
    for a in G.nodes:
        for d in G.nodes:
            if a == d:
                continue
            # Find all simple paths up to length 5
            for path in nx.all_simple_paths(G, source=a, target=d, cutoff=5):
                if len(path) < 3:
                    continue
                # Check if path is [sibling, sibling, ..., parent]
                rel_chain = [G[path[i]][path[i+1]]['relation'] for i in range(len(path)-1)]
                if len(rel_chain) >= 2 and all(r in ('brother', 'sister', 'sibling') for r in rel_chain[:-1]) and rel_chain[-1] in ('father', 'mother', 'parent'):
                    ua_type = 'uncle' if gender_map.get(a) == 'male' else 'aunt' if gender_map.get(a) == 'female' else 'uncle/aunt'
                    indirect.append({'from': a, 'to': d, 'relation': ua_type, 'via': path[1:-1]})
    # Grandparent/Grandchild
    for a in G.nodes:
        for b in G.successors(a):
            rel1 = G[a][b]['relation']
            for c in G.successors(b):
                rel2 = G[b][c]['relation']
                if rel1 in ('father', 'mother', 'parent') and rel2 in ('father', 'mother', 'parent'):
                    gp_type = 'grandfather' if gender_map.get(a) == 'male' else 'grandmother' if gender_map.get(a) == 'female' else 'grandparent'
                    indirect.append({'from': a, 'to': c, 'relation': gp_type, 'via': b})
                if rel1 in ('son', 'daughter', 'child') and rel2 in ('son', 'daughter', 'child'):
                    gc_type = 'grandson' if gender_map.get(a) == 'male' else 'granddaughter' if gender_map.get(a) == 'female' else 'grandchild'
                    indirect.append({'from': a, 'to': c, 'relation': gc_type, 'via': b})
    # Multi-hop cousin: A is B's parent, B is C's sibling (possibly multi-hop), C is D's child => A and D are cousins
    for a in G.nodes:
        for d in G.nodes:
            if a == d:
                continue
            for path in nx.all_simple_paths(G, source=a, target=d, cutoff=5):
                if len(path) < 4:
                    continue
                rel_chain = [G[path[i]][path[i+1]]['relation'] for i in range(len(path)-1)]
                # [parent, sibling, ..., sibling, child]
                if rel_chain[0] in ('father', 'mother', 'parent') and rel_chain[-1] in ('son', 'daughter', 'child') and all(r in ('brother', 'sister', 'sibling') for r in rel_chain[1:-1]):
                    indirect.append({'from': a, 'to': d, 'relation': 'cousin', 'via': path[1:-1]})
    # Niece/Nephew: A is B's sibling, B is C's parent, C is D's child => D is A's niece/nephew
    for a in G.nodes:
        for b in G.successors(a):
            rel1 = G[a][b]['relation']
            if rel1 in ('brother', 'sister', 'sibling'):
                for c in G.successors(b):
                    rel2 = G[b][c]['relation']
                    if rel2 in ('father', 'mother', 'parent'):
                        for d in G.successors(c):
                            rel3 = G[c][d]['relation']
                            if rel3 in ('son', 'daughter', 'child'):
                                nn_type = 'nephew' if gender_map.get(d) == 'male' else 'niece' if gender_map.get(d) == 'female' else 'niece/nephew'
                                indirect.append({'from': d, 'to': a, 'relation': nn_type, 'via': (b, c)})
    # Parent/child through sibling: A is B's parent, B is C's sibling => A is C's parent
    for a in G.nodes:
        for b in G.successors(a):
            rel1 = G[a][b]['relation']
            if rel1 in ('father', 'mother', 'parent'):
                for c in G.successors(b):
                    rel2 = G[b][c]['relation']
                    if rel2 in ('brother', 'sister', 'sibling'):
                        pc_type = 'father' if gender_map.get(a) == 'male' else 'mother' if gender_map.get(a) == 'female' else 'parent'
                        indirect.append({'from': a, 'to': c, 'relation': pc_type, 'via': b})
    # In-law (spouse's parent/child, robust gender)
    for a in G.nodes:
        for b in G.successors(a):
            rel1 = G[a][b]['relation']
            if rel1 in ('husband', 'wife'):
                spouse_gender = 'male' if rel1 == 'husband' else 'female' if rel1 == 'wife' else None
                for c in G.successors(b):
                    rel2 = G[b][c]['relation']
                    if rel2 in ('father', 'mother', 'parent'):
                        il_type = 'father-in-law' if spouse_gender == 'male' or (spouse_gender is None and gender_map.get(a) == 'male') else 'mother-in-law'
                        indirect.append({'from': a, 'to': c, 'relation': il_type, 'via': b})
                    if rel2 in ('son', 'daughter', 'child'):
                        sil_type = 'son-in-law' if spouse_gender == 'male' or (spouse_gender is None and gender_map.get(a) == 'male') else 'daughter-in-law'
                        indirect.append({'from': a, 'to': c, 'relation': sil_type, 'via': b})
    # Step relationships (placeholder)
    # ...
    return indirect 