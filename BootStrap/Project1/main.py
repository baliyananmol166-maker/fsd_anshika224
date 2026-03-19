import streamlit as st
st.title("Streamlit Tutorial")
st.write("Hello")
st.header("Header")
st.subheader("Sub Header")
st.code("#include<stdio.h>")
st.caption("This is caption")
st.button("Click Me")
st.radio("Select",["Option 1","Option 2","Option 3"])
st.selectbox("Select",["Option 1","Option 2","Option 3"])
st.select_slider("Select",["Option 1","Option 2","Option 3"])

st.checkbox("Select",["A"])
i= st.text_input("Enter data")
if i:
    st.write(i)
