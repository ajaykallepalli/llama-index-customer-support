import streamlit as st
from support_ai import SupportAI

st.set_page_config(page_title="Customer Support AI (Streamlit)")

@st.cache_resource
def get_support_ai():
    return SupportAI()

support_ai = get_support_ai()

st.title("Customer Support AI (Streamlit)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = support_ai.get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)