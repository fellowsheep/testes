import streamlit as st

st.write('Hello, *World!* :sunglasses:')

st.write('Qual é o seu nome?')
nome = st.text_input('Nome','')
st.write('Olá, ', nome, '!!')

st.image('./Logosheep.png',width=100)

