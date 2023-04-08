import streamlit as st

st.title('Largest among the three numbers: ')
st.text("")
st.text("")
st.text("")
a = st.number_input(label='Enter the first Number',step=1)
st.text("")
b = st.number_input(label='Enter the second Number',step=1)
st.text("")
c = st.number_input(label='Enter the third Number',step=1)

if st.button(label="Submit"):
    st.text("The largest number among the given input is: ")
    if(a>=b):
        if(a>=c):
            st.text(a)
        else:
            st.text(c)
    else:
        if(b>=c):
            st.text(b)
        else:
            st.text(c)
