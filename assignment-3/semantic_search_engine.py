from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
knowledge_base = [
    "To reset your password, click on Forgot Password on the login page.",
    "Billing invoices can be downloaded from the billing section.",
    "You can update your email address from account settings.",
    "Two-factor authentication improves account security.",
    "If your account is locked, contact customer support.",
    "Subscription plans can be upgraded anytime.",
    "Login issues may occur due to incorrect credentials.",
    "Refund requests are processed within seven business days.",
    "Users can manage notifications from profile settings.",
    "Payment failures may happen if the card has expired."
]
print("Loading embedding model")
model = SentenceTransformer("./all-MiniLM-L6-v2")
print("Model loaded successfully")
embeddings=model.encode(knowledge_base, convert_to_numpy=True)
print("\nEmbedding Matrix Shape:")
print(embeddings.shape)
dimension=embeddings.shape[1]
index=faiss.IndexFlatL2(dimension)
embeddings=np.array(embeddings).astype("float32")
faiss.normalize_L2(embeddings)
index.add(embeddings)
print("\nTotal vectors in index:")
print(index.ntotal)
sample_queries=[
    "How do I change my password?",
    "My payment is failing",
    "I cannot login to my account"
]
for query in sample_queries:
    query_embedding=model.encode([query],convert_to_numpy=True)
    query_embedding=np.array(query_embedding).astype("float32")
    faiss.normalize_L2(query_embedding)
    distances,indices=index.search(query_embedding,k=3)
    print(f"\nQuery: {query}")
    print("-"*70)
    print("Rank | Score | Matched Sentence")
    print("-"*70)
    for rank,idx in enumerate(indices[0]):
        score=distances[0][rank]
        print(f"{rank+1} | {score:.4f} | {knowledge_base[idx]}")
print("\n===================================")
print("Semantic Search CLI")
print("Type 'exit' to quit")
print("===================================")
while True:
    query=input("\nEnter Query: ")
    if query.lower()=="exit":
        print("Goodbye!")
        break
    query_embedding=model.encode([query])
    query_embedding=np.array(query_embedding).astype("float32")
    faiss.normalize_L2(query_embedding)
    distances,indices=index.search(query_embedding,k=3)
    print("\nTop 3 Results")
    print("-" * 70)
    print("Rank | Score | Matched Sentence")
    print("-" * 70)
    for rank,idx in enumerate(indices[0]):
        score=distances[0][rank]
        print(f"{rank+1} | {score:.4f} | {knowledge_base[idx]}")