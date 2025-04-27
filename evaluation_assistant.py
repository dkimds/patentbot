import streamlit as st
from modules.streamlit_app import main

st.title("Patent Evaluation Assistant")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # Upload patent
    bytes_data = uploaded_file.getvalue()
    file_path = "./temp.pdf"
    with open(file_path, "wb") as f:
        f.write(bytes_data)

with st.form("my_form"):
    text = st.text_area(
        "Enter topic:",
        "The business feasibility of adopting the following patent as a business model",)
    submitted = st.form_submit_button("Submit")
    if submitted:
        main(text)