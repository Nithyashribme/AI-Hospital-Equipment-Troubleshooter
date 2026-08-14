# 5-Minute Demo Script

## 0:00–0:30 — Problem
"Biomedical engineering students study hospital equipment theoretically, but connecting theory to practical troubleshooting can be difficult. I built this educational prototype to demonstrate a structured approach to common equipment faults."

## 0:30–1:00 — What I built
"This is a Streamlit web application. The user selects equipment and describes a symptom. The application analyzes the symptom against a curated knowledge base and returns possible causes, basic checks, and safety guidance."

## 1:00–2:30 — Live demo
1. Select ECG Machine.
2. Enter: "ECG machine is not printing."
3. Click Analyze Problem.
4. Show causes, checks, and safety.
5. Try a second example such as ventilator flow-sensor problem.

## 2:30–3:30 — Technical explanation
"The first version uses Python, Streamlit and a JSON knowledge base. I intentionally used controlled troubleshooting content instead of allowing a model to invent repair instructions. The matching layer identifies relevant fault categories from the symptom."

## 3:30–4:15 — AI usage
"I used AI tools during development to brainstorm features, assist with code generation, debug issues, improve the interface and documentation. I reviewed and adapted the output rather than treating AI output as automatically correct."

## 4:15–5:00 — Future development
"The next version can use RAG with approved manufacturer manuals. The system could retrieve relevant manual sections, pass them to an LLM, and return an answer with citations. This would make the system more flexible while keeping the information source controlled."
