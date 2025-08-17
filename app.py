import streamlit as st

st.title('Power Calculator')

st.write('Enter a number to calculate its square, cube and fifth power')

n = st.number_input('Enter an integer', value=1, step = 1)

square = n*n
cube = n*n*n
fifth = n*n*n*n*n

st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth power of {n} is {fifth}")