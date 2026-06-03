# Conversational RAG Assistant

## Project Overview

This project is a simple Conversational RAG (Retrieval-Augmented Generation) Assistant built using Python.

The assistant can:

- Read and understand content from a PDF document
- Answer questions using information from the PDF
- Remember previous conversations
- Handle follow-up questions
- Call external tools when needed

For this project, I implemented a Time Tool that returns the current date and time.

---

## How It Works

### Step 1: Load PDF

The PDF document is loaded using PyPDFLoader.

### Step 2: Split Text into Chunks

The document is divided into smaller chunks so that relevant information can be retrieved easily.

### Step 3: Create Embeddings

TF-IDF Vectorizer is used to convert text chunks into vectors.

### Step 4: Retrieve Relevant Context

When a user asks a question, cosine similarity is used to find the most relevant chunk from the document.

### Step 5: Conversation Memory

The assistant stores previous questions and answers in chat history.

This helps it understand follow-up questions such as:

User: What is RAG?

User: Explain it more.

The assistant understands that "it" refers to RAG.

### Step 6: Tool Calling

If the question cannot be answered from the document, the assistant checks whether an external tool should be used.

Example:

User: What is the current time?

The assistant calls the Time Tool and returns the result.

---

## Tool Used

### get_current_time()

Returns the current system date and time.

Example:

Current Time: 2026-06-03 10:30:45

---

## Project Structure
