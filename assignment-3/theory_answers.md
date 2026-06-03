# FAISS Theory Answers

## Q1. Difference between IndexFlatL2 and IndexFlatIP

### IndexFlatL2

Uses Euclidean Distance (L2 Distance).

Smaller distance means vectors are more similar.

Example:

Distance(A,B) = sqrt((x2-x1)^2 + (y2-y1)^2)

### IndexFlatIP

Uses Inner Product (Dot Product).

Higher score means vectors are more similar.

### When to Use

- Use IndexFlatL2 when Euclidean distance is required.
- Use IndexFlatIP when using cosine similarity with normalized vectors.

---

## Q2. Why normalize embeddings?

Cosine similarity depends only on vector direction.

Normalization converts vectors to unit length.

This removes the effect of vector magnitude and allows similarity comparison based only on semantic meaning.

Without normalization, vectors with larger magnitudes may appear more similar even when they are not.

---

## Q3. What is Approximate Nearest Neighbor (ANN)?

Approximate means FAISS may not always return the exact nearest vector.

Instead, it returns a very close match much faster.

Why acceptable?

- Massive speed improvement
- Lower memory usage
- Scales to millions or billions of vectors
- Small loss in accuracy is usually acceptable in production systems

This is why ANN is widely used in modern RAG applications.