# Semantic Search Engine using FAISS

## Objective

Build a mini semantic search engine using FAISS as the vector store. Generate embeddings using Sentence Transformers, store them in FAISS, and perform semantic similarity search.

---

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- NumPy

---

# Task 1 - Setup & Embedding Generation

Created a knowledge base containing 10 support-related sentences covering:

- Password Reset
- Billing
- Account Management
- Login Issues
- Security
- Subscription Plans
- Refunds
- Notifications
- Payments

Generated embeddings using the `all-MiniLM-L6-v2` model.

### Output

```text
Loading embedding model
Model loaded successfully

Embedding Matrix Shape:
(10, 384)
```

---

# Task 2 - Build a FAISS Index

Created a FAISS IndexFlatL2 index with embedding dimension 384.

Normalized embeddings using:

```python
faiss.normalize_L2(embeddings)
```

Added embeddings to the index.

### Output

```text
Total vectors in index:
10
```

---

# Task 3 - Semantic Search with FAISS

## Query 1

```text
How do I change my password?
```

### Output

```text
Rank | Score | Matched Sentence
------------------------------------------------------
1 | 0.2145 | To reset your password, click on Forgot Password on the login page.
2 | 0.4871 | Login issues may occur due to incorrect credentials.
3 | 0.6352 | You can update your email address from account settings.
```

---

## Query 2

```text
My payment is failing
```

### Output

```text
Rank | Score | Matched Sentence
------------------------------------------------------
1 | 0.1763 | Payment failures may happen if the card has expired.
2 | 0.5128 | Billing invoices can be downloaded from the billing section.
3 | 0.6891 | Refund requests are processed within seven business days.
```

---

## Query 3

```text
I cannot login to my account
```

### Output

```text
Rank | Score | Matched Sentence
------------------------------------------------------
1 | 0.1428 | Login issues may occur due to incorrect credentials.
2 | 0.4021 | If your account is locked, contact customer support.
3 | 0.5984 | To reset your password, click on Forgot Password on the login page.
```

---

# Task 4 - Interactive CLI

Implemented a continuous query loop where users can enter queries until they type `exit`.

### Sample Run

```text
===================================
Semantic Search CLI
Type 'exit' to quit
===================================

Enter Query: forgot my password

Top 3 Results

Rank | Score | Matched Sentence
------------------------------------------------------
1 | 0.2014 | To reset your password, click on Forgot Password on the login page.
2 | 0.4912 | Login issues may occur due to incorrect credentials.
3 | 0.6224 | If your account is locked, contact customer support.

Enter Query: exit

Goodbye!
```

---

# Files Included

```text
assignment-3/
│
├── semantic_search_engine.py
├── README.md
├── theory_answers.md
└── screenshots/
```
