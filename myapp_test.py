import streamlit as st
import pandas as pd

st.write("""Test App Machine Learning""")
#added comment
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

st.metric("Accuracy", "90%", "+2.5")


df = pd.read_csv('Lab2_prepared.csv')
result = "perfect"

if st.button('Predict'):
  st.write(result)


st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

options = st.multiselect('Category',['Car', 'Bus',
'Train', 'Airplane'],['Car', 'Bus'])
st.write('You selected:', options)

