from pathlib import Path


def load_documents(folder):
    """Read every .md / .txt file in a folder."""
    docs = []
    for path in sorted(Path(folder).rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            docs.append({"source": path.name, "text": text})
    return docs


def chunk_text(text, chunk_size=800):
    """Split text into chunks, keeping paragraphs together."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""

    for para in paragraphs:
        # if adding this paragraph still fits, add it to the current chunk
        if len(current) + len(para) <= chunk_size:
            current = (current + "\n\n" + para).strip()
        else:
            chunks.append(current)   # chunk is full, save it
            current = para           # start a new chunk
    if current:
        chunks.append(current)       # don't forget the last one
    return chunks


def build_chunks(folder):
    """Return a list of {id, text, source} for every chunk."""
    all_chunks = []
    for doc in load_documents(folder):
        for i, chunk in enumerate(chunk_text(doc["text"])):
            all_chunks.append({
                "id": f"{doc['source']}::{i}",   # unique id per chunk
                "text": chunk,
                "source": doc["source"],          # remember which file it came from
            })
    return all_chunks