import pandas as pd 
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

st.title("San francisco Map")
st.header("Using Streamlit and Mapbox")

map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)