import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3


connection = sqlite3.Connection("data.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM temp_data")
values = cursor.fetchall()
dates = [value[0] for value in values]
temperatures = [value[1] for value in values]

# df= pd.read_csv("temp_data.txt")
figure = px.line(x=dates,y=temperatures,labels={'x':'Date','y':'Temperatures'})
st.plotly_chart(figure)
