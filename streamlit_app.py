import streamlit as st

st.write('Hello, *World!* :sunglasses:')

st.write('Qual é o seu nome?')
nome = st.text_input()
st.write('Olá, ', nome, '!!')
