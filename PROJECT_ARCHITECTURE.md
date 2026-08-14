# Project Architecture

User
  ↓
Streamlit Interface
  ↓
Equipment + Symptom Input
  ↓
Keyword Matching Layer
  ↓
Curated JSON Knowledge Base
  ↓
Possible Causes + Basic Checks + Safety Guidance
  ↓
User

Future AI/RAG architecture:

User Query
  ↓
Embedding / Retrieval
  ↓
Approved Equipment Manuals
  ↓
Relevant Context
  ↓
LLM
  ↓
Structured Answer + Citations + Safety Note
