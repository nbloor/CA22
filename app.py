import streamlit as st
import pandas as ps
import numpu as np

st.title("Simple Streamlit App")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
}))

if st.button('Say hello'):
  st.write('Why hellow there'!)
else:
  st.write('Goodbye')

char_data = pd.DataFrame(
  np.random = randn(20, 3),
  columns=['a', 'b', 'c'])

st.line_chart(chart_data)
