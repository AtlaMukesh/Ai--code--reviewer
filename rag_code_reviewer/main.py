import os
import streamlit as st
from dotenv import load_dotenv

from rag.vectorstore import GuidelineStore
from rag.retriever import retrieve_guidelines
from rag.reviewer import review_code

load_dotenv()   # reads the .env file

st.set_page_config(page_title="AI Code Reviewer", layout="wide")


@st.cache_resource          # create the store once, not on every click
def get_store():
    store = GuidelineStore()
    if store.count() == 0:
        store.index_folder("guidelines")
    return store


store = get_store()

# ---- sidebar ----
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Anthropic API key", type="password",
                            value=os.getenv("ANTHROPIC_API_KEY", ""))
    language = st.selectbox("Language", ["Python", "JavaScript", "Java", "C++"])
    top_k = st.slider("Guideline chunks", 1, 8, 4)
    if st.button("Re-index guidelines"):
        st.success(f"Indexed {store.index_folder('guidelines')} chunks")

# ---- main page ----
st.title("AI-Powered Code Reviewer")
code = st.text_area("Paste your code", height=300)

if st.button("Review my code", type="primary"):
    if not code.strip():
        st.warning("Paste some code first.")
    elif not api_key:
        st.warning("Add your API key in the sidebar.")
    else:
        with st.spinner("Reviewing..."):
            guidelines = retrieve_guidelines(store, code, language, k=top_k)
            try:
                review = review_code(code, language, guidelines, api_key=api_key)
            except Exception as e:
                st.error(f"Review failed: {e}")
                st.stop()

        st.markdown(review)

        with st.expander("Guidelines used"):
            for g in guidelines:
                st.markdown(f"**{g['source']}**")
                st.text(g["text"])
            