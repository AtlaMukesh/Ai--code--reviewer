import chromadb
from .loader import build_chunks   # the dot means "from this same package"

COLLECTION_NAME = "code_guidelines"


class GuidelineStore:
    def __init__(self, persist_dir="chroma_db"):
        # PersistentClient saves the database to disk in the chroma_db folder
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(COLLECTION_NAME)

    def index_folder(self, folder):
        """Read the guidelines folder and store all chunks."""
        chunks = build_chunks(folder)
        if not chunks:
            return 0

        # delete the old collection so edited files don't leave stale data
        self.client.delete_collection(COLLECTION_NAME)
        self.collection = self.client.get_or_create_collection(COLLECTION_NAME)

        self.collection.add(
            ids=[c["id"] for c in chunks],
            documents=[c["text"] for c in chunks],
            metadatas=[{"source": c["source"]} for c in chunks],
        )
        return len(chunks)

    def count(self):
        return self.collection.count()

    def query(self, text, k=4):
        """Find the k chunks whose meaning is closest to `text`."""
        if self.count() == 0:
            return []
        result = self.collection.query(
            query_texts=[text],
            n_results=min(k, self.count()),
        )
        docs = result["documents"][0]
        metas = result["metadatas"][0]
        return [{"text": d, "source": m["source"]} for d, m in zip(docs, metas)]