# AI Meeting Prep Agent (RAG + Memory + Tools)

## Objective
This project builds an AI agent that prepares users for client meetings using:
- Retrieval-Augmented Generation (FAISS)
- Short-term memory (session context)
- Long-term memory (persistent storage)
- Tool-based agent workflow

---

## Features

### 1. RAG System
Uses FAISS vector database with sentence-transformer embeddings to retrieve relevant client information.

### 2. Short-Term Memory
Stores conversation history within the session.

### 3. Long-Term Memory
Stores generated meeting briefs for future reference.

### 4. Tools Used
- Document Search Tool (FAISS)
- Meeting Notes Retriever
- Memory System

---

## Sample Query

**Input:**
Prepare me for my meeting with Acme Corp

**Output:**

MEETING PREPARATION BRIEF
-------------------------
User Query: Prepare me for my meeting with Acme Corp

KEY CLIENT INFO:
- Acme Corp is a SaaS company focused on CRM tools.
- Decision maker is John Smith, CTO.

PREVIOUS NOTES:
- Meeting on March: discussed integration timeline.
- Client asked for discount approval.

CONVERSATION CONTEXT:
- Prepare me for my meeting with Acme Corp

NEXT STEPS:
1. Review client history
2. Focus on open action items
3. Prepare pricing discussion

---

