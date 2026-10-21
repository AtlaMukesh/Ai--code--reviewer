# AI-Powered Code Reviewer

A RAG-based code review tool. You paste code, and it reviews it using your own
guideline documents, which are retrieved from a ChromaDB vector store.
The review is written by Google Gemini.

## How it works
1. Guideline files in the guidelines folder are split into chunks and stored in ChromaDB.
2. When you submit code, the most relevant guideline chunks are retrieved.
3. Gemini reviews the code using those guidelines and returns issues, fixes and a score.

## Setup
1. Install the libraries: pip install -r requirements.txt
2. Create a .env file with one line: GEMINI_API_KEY=your_key
3. Run: cd rag_code_reviewer, then streamlit run main.py

## Tech
Python, Streamlit, ChromaDB, Google Gemini API
