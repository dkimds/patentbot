import streamlit as st
from modules.streamlit_app import main

st.title("Patent Evaluation Assistant")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    file_path = "./temp.pdf"
    with open(file_path, "wb") as f:
        f.write(bytes_data)

# Session state에 count가 없으면 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

with st.form("my_form"):
    text = st.text_area(
        "Enter topic:",
        "The business feasibility of adopting the following patent as a business model",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.count += 1
        main(text, st.session_state.count)
