import streamlit as st
import pandas as pd
import plotly.express as px

df= pd.read_csv("temp_data.txt")
figure = px.line(x=df['date'],y=df['temperatures'],labels={'x':'Date','y':'Temperatures'})
st.plotly_chart(figure)
