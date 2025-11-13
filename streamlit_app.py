import streamlit as st

st.title("🎈 Updated Title")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

name = st.text_input("Enter your name: ")
if name:
    st.success(f"Hello, {name}! Welcome to the new page!")
else:
    st.error(f"Please enter your name...")