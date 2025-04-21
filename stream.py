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
st.subheader("📄 Filtered Dataset")
st.dataframe(filtered_df)

# Avg Price by Brand
st.subheader("💸 Average Price by Brand")
brand_price = filtered_df.groupby("name")["price"].mean().reset_index()
fig1 = px.bar(brand_price, x="name", y="price", title="Average Price per Brand", color="price")
st.plotly_chart(fig1, use_container_width=True)

# Price vs Year Scatter
st.subheader("📈 Price vs Year")
fig2 = px.scatter(filtered_df, x="year", y="price", color="fuel", hover_data=["name"], title="Price vs Year")
st.plotly_chart(fig2, use_container_width=True)

# ✅ NEW CHARTS BELOW

# Fuel Type Pie Chart
st.subheader("⛽ Fuel Type Distribution")
fuel_count = filtered_df['fuel'].value_counts().reset_index()
fig3 = px.pie(fuel_count, names='index', values='fuel', title='Fuel Type Share')
st.plotly_chart(fig3, use_container_width=True)

# Average Price by Year (Line)
st.subheader("📅 Avg Price Over Years")
yearly_avg = filtered_df.groupby("year")["price"].mean().reset_index()
fig4 = px.line(yearly_avg, x="year", y="price", title="Average Price by Year")
st.plotly_chart(fig4, use_container_width=True)

# Price Boxplot by Fuel Type
st.subheader("📦 Price Distribution by Fuel Type")
fig5 = px.box(filtered_df, x="fuel", y="price", title="Boxplot: Price vs Fuel Type", color="fuel")
st.plotly_chart(fig5, use_container_width=True)

# Histogram of KM Driven
st.subheader("🚘 KM Driven Histogram")
fig6 = px.histogram(filtered_df, x="km_driven", nbins=30, title="Kilometers Driven Distribution", color_discrete_sequence=["indianred"])
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Plotly | Demo Dataset")
