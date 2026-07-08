import streamlit as st

from app.guardrail import check_guardrail
from app.agent import run_agent

st.set_page_config(
    page_title="HobbyFi AI Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 HobbyFi AI Copilot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask something...")

if query:

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    decision = check_guardrail(query)

    if decision != "ALLOW":
        answer = "❌ Request blocked by Guardrail."
    else:
        answer = run_agent(query)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })