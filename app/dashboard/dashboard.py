import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Laplace - Bike Market Intelligence")

df = pd.read_csv("data/bike_data.csv")

st.subheader("Price Distribution")
fig = px.histogram(df, x="price")
st.plotly_chart(fig)

st.subheader("Top Brands")
brand_counts = df["brand"].value_counts().head(10)
st.bar_chart(brand_counts)
