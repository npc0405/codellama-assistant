import streamlit as st
from assistant import generate_code, explain_code, fix_bug, optimize_code

st.set_page_config(page_title="CodeLlama Code Assistant", layout="wide")

st.title("CodeLlama Code Assistant")
st.caption("Powered by local CodeLlama (via Ollama)")

task_type = st.selectbox(
    "Choose a task type:",
    ["Generate Code", "Explain Code", "Debug Code", "Optimize Code"]
)

placeholder_text = {
    "Generate Code": "Describe what the code should do (e.g. 'a function to check prime numbers')",
    "Explain Code": "Paste the code you want to be explained",
    "Debug Code": "Paste the buggy code here",
    "Optimize Code": "Paste the code you want optimized",
}

user_input = st.text_area("Code / Prompt", height=250, placeholder=placeholder_text[task_type])

error_message = ""
if task_type == "Debug Code":
    error_message = st.text_input("Error message (optional)")

if st.button("Run", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some code or a prompt first.")
    else:
        with st.spinner("Thinking..."):
            if task_type == "Generate Code":
                result = generate_code(user_input)
            elif task_type == "Explain Code":
                result = explain_code(user_input)
            elif task_type == "Debug Code":
                result = fix_bug(user_input, error_message)
            elif task_type == "Optimize Code":
                result = optimize_code(user_input)

        st.subheader("Output")
        st.markdown(result)