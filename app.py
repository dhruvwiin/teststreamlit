import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.title("Hello World App")
st.write("This is a simple Streamlit app.")
st.button("Click me!")
if st.file_uploader("Upload CSV", type=["csv"]):
    data = pd.read_csv("data.csv")
    st.write(data)
