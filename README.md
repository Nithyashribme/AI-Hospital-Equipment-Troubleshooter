# 🏥 AI Hospital Equipment Troubleshooter

## Overview
**AI Hospital Equipment Troubleshooter** is a student-built educational web application that helps biomedical engineering students understand common hospital-equipment fault scenarios.

The user selects an equipment category and describes a symptom in natural language. The application maps the symptom to a curated troubleshooting knowledge base and presents possible causes, basic non-invasive checks, and safety guidance.

## Problem Statement
Biomedical engineering students learn equipment theory but may find it difficult to connect that theory with practical fault-identification. A simple interactive tool can help learners practice a structured troubleshooting approach.

## Objectives
1. Provide a simple interface for describing equipment symptoms.
2. Organize common faults into a searchable knowledge base.
3. Present possible causes and safe first checks.
4. Emphasize escalation and safety.
5. Demonstrate how AI-assisted development can be combined with biomedical engineering knowledge.

## Equipment Covered
- ECG Machine
- Patient Monitor
- Infusion Pump
- Ventilator
- Defibrillator
- Hemodialysis Machine
- Suction Machine

## Key Features
- Equipment selection
- Natural-language symptom entry
- Keyword-based issue matching
- Possible-cause analysis
- Basic-check guidance
- Safety warnings
- Recent troubleshooting history
- Responsive Streamlit interface
- Modular JSON knowledge base

## Technology Stack
- Python
- Streamlit
- JSON
- GitHub

## How AI Was Used
AI tools were used as a development assistant for:
- brainstorming the problem and feature set
- suggesting application structure
- generating and refining code
- debugging and improving the user interface
- preparing documentation

The equipment guidance was organized as a curated knowledge base rather than allowing an uncontrolled model to invent repair instructions.

## How to Run

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Hospital-Equipment-Troubleshooter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```

## Example
**Input:**  
Equipment: ECG Machine  
Problem: "The ECG machine is not printing."

**Output:**  
- Possible causes
- Basic checks
- Safety guidance
- Escalation recommendation

## Safety and Scope
This is an **educational portfolio prototype**. It is not a medical device, clinical decision-support system, repair manual, or substitute for qualified technical service.

Do not:
- bypass safety alarms
- open equipment for internal repair
- change clinical settings without authorization
- use the tool to make patient-care decisions

Always follow the exact device manual, hospital SOP, and qualified biomedical/technical procedures.

## Future Improvements
- Retrieval-Augmented Generation (RAG) using approved equipment manuals
- LLM-based natural-language understanding
- Source citations for every retrieved instruction
- PDF/manual upload
- User feedback and issue reporting
- Multilingual explanations
- Authentication and role-based access
- Evaluation dataset for troubleshooting accuracy

## Author
Biomedical Engineering Student — Portfolio Project
