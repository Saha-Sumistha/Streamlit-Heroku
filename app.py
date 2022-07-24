import streamlit as st

st.title('Find whether the given number is odd or even')
a = st.number_input('Enter a number')
result="not an integer"
if (a).is_integer():
    if a%2==0:
        result="Even"
    else:
        result="Odd"
else:
    st.write("Please enter an integer input")
st.write("This number is ", result,"number.")