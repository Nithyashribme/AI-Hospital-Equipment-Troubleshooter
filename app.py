import json
from pathlib import Path
from datetime import datetime
import streamlit as st

st.set_page_config(
    page_title="AI Hospital Equipment Troubleshooter",
    page_icon="🏥",
    layout="wide"
)

BASE = Path(__file__).parent
with open(BASE / "equipment_data.json", "r", encoding="utf-8") as f:
    EQUIPMENT = json.load(f)

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Styling ----------
st.markdown("""
<style>
.main-title {font-size: 2.2rem; font-weight: 700; margin-bottom: 0.2rem;}
.subtitle {color: #5f6368; font-size: 1rem;}
.card {
    padding: 1rem; border-radius: 12px; border: 1px solid #ddd;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="main-title">🏥 AI Hospital Equipment Troubleshooter</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">An educational decision-support prototype for biomedical engineering students</div>',
    unsafe_allow_html=True
)

st.info(
    "⚠️ Educational prototype only. It does not diagnose patients, authorize repairs, "
    "or replace hospital SOPs, manufacturer manuals, clinical judgment, or qualified biomedical/technical personnel."
)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Project")
    st.write("Version 1.0")
    st.write("Knowledge-base troubleshooting prototype")
    st.divider()
    st.subheader("Equipment covered")
    for item in EQUIPMENT:
        st.write("• " + item)
    st.divider()
    if st.button("Clear history"):
        st.session_state.history = []
        st.rerun()

# ---------- Main ----------
left, right = st.columns([1, 1])

with left:
    st.subheader("1️⃣ Describe the problem")
    equipment = st.selectbox("Equipment", list(EQUIPMENT.keys()))
    problem = st.text_area(
        "Symptom / issue",
        placeholder="Example: ECG machine is not printing.",
        height=130
    )

    troubleshoot = st.button("🔍 Analyze Problem", use_container_width=True)

with right:
    st.subheader("2️⃣ Troubleshooting result")

    if troubleshoot:
        if not problem.strip():
            st.warning("Please describe the symptom.")
        else:
            text = problem.lower()
            matched = None

            for issue in EQUIPMENT[equipment]:
                if any(keyword in text for keyword in issue["keywords"]):
                    matched = issue
                    break

            if matched:
                st.success(f"Matched issue: {matched['name']}")

                with st.expander("🔎 Possible causes", expanded=True):
                    for item in matched["causes"]:
                        st.write("• " + item)

                with st.expander("🛠️ Basic checks", expanded=True):
                    for item in matched["checks"]:
                        st.write("• " + item)

                with st.expander("⚠️ Safety guidance", expanded=True):
                    st.write(matched["safety"])

                result = {
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "equipment": equipment,
                    "problem": problem,
                    "issue": matched["name"]
                }
                st.session_state.history.insert(0, result)
            else:
                st.warning(
                    "No matching common fault was found in the prototype knowledge base."
                )
                st.write(
                    "Review the manufacturer's instructions and hospital SOP. "
                    "If the equipment is not safe or the fault persists, escalate to "
                    "qualified biomedical/technical personnel."
                )

# ---------- Learning section ----------
st.divider()
st.subheader("📚 Learn about the selected equipment")

with st.expander("What this prototype demonstrates"):
    st.write(
        "The application accepts a natural-language symptom, searches a curated "
        "equipment knowledge base using keywords, and returns structured troubleshooting "
        "guidance. A future version can replace this matching layer with RAG + an LLM "
        "using approved equipment manuals."
    )

# ---------- History ----------
if st.session_state.history:
    st.divider()
    st.subheader("🕘 Recent checks")
    for item in st.session_state.history[:5]:
        st.write(
            f"**{item['equipment']}** — {item['problem']} → `{item['issue']}` "
            f"({item['time']})"
        )

st.divider()
st.caption(
    "Built as a student portfolio project | Biomedical Engineering + AI | "
    "Always follow the specific device manual and hospital policy."
)
