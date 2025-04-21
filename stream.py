import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🚗 Used Car Price Explorer")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("cars.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
brands = st.sidebar.multiselect("Select Car Brands", options=df["name"].unique(), default=df["name"].unique())
fuel_types = st.sidebar.multiselect("Select Fuel Type", options=df["fuel"].unique(), default=df["fuel"].unique())

filtered_df = df[(df["name"].isin(brands)) & (df["fuel"].isin(fuel_types))]

# Show filtered data
st.subheader("Filtered Dataset")
st.dataframe(filtered_df)

# Plot: Average Price by Brand
st.subheader("💸 Average Price by Brand")
brand_price = filtered_df.groupby("name")["price"].mean().reset_index()
fig1 = px.bar(brand_price, x="name", y="price", title="Average Price per Brand", color="price")
st.plotly_chart(fig1, use_container_width=True)

# Plot: Price vs Year
st.subheader("📈 Price Distribution by Year")
fig2 = px.scatter(filtered_df, x="year", y="price", color="fuel", hover_data=["name"], title="Price vs Year")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Plotly | Demo Dataset")
