import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Family Relationship Reasoning", layout="wide")
st.title("Family Relationship Reasoning Demo")

API_URL = "http://localhost:8000/analyze"

with st.form("analyze_form"):
    text = st.text_area("Enter family relationship text:", height=150)
    question = st.text_input("Optional: Ask a question (e.g., 'How is Alice related to Bob?')")
    submitted = st.form_submit_button("Analyze")

if submitted and text.strip():
    with st.spinner("Analyzing..."):
        try:
            resp = requests.post(API_URL, json={"text": text, "question": question})
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            st.error(f"API error: {e}")
            st.stop()

    st.subheader("Entities")
    st.write([n["text"] for n in data["nodes"]])

    st.subheader("Relationships")
    st.write([{k: e[k] for k in ("source", "target", "text")} for e in data["edges"]])

    if data.get("answer"):
        st.success(f"**Answer:** {data['answer']}")
    if data.get("reasoning"):
        st.info("\n".join(data["reasoning"]))

    # Draw graph
    st.subheader("Relationship Graph")
    G = nx.DiGraph()
    label_map = {n["id"]: n["text"] for n in data["nodes"]}
    for n in data["nodes"]:
        G.add_node(n["id"])
    for e in data["edges"]:
        G.add_edge(e["source"], e["target"], label=e["text"])
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, labels={k: v for k, v in label_map.items()}, with_labels=True, node_color="#90caf9", node_size=1200, font_size=12, font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    st.pyplot(plt.gcf())
    plt.clf()

    st.caption("Powered by FastAPI, Gemini, and symbolic reasoning.")
else:
    st.info("Enter some text and click Analyze to get started.") 