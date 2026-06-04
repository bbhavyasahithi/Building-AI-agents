from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model=SentenceTransformer("./all-MiniLM-L6-v2")
def build_index(docs):
    embeddings=model.encode(docs)
    embeddings=np.array(embeddings).astype("float32")
    faiss.normalize_L2(embeddings)
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index,docs
def search(query,index,docs,k=3):
    q_emb=model.encode([query])
    q_emb=np.array(q_emb).astype("float32")
    faiss.normalize_L2(q_emb)
    scores,idx=index.search(q_emb,k)
    return [(docs[i], scores[0][j]) for j, i in enumerate(idx[0])]