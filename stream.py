import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🌍 COVID-19 Live Dashboard")

# Load data from API
@st.cache_data(ttl=3600)
def load_data():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    data = response.json()
    return data

data = load_data()

# Convert to DataFrame
countries_df = pd.DataFrame(data['Countries'])

# Country selector
country = st.selectbox("Select a country", countries_df['Country'].sort_values())

# Filter selected country data
selected = countries_df[countries_df['Country'] == country].squeeze()

# Display metrics
st.subheader(f"COVID-19 Status in {country}")
col1, col2, col3 = st.columns(3)
col1.metric("Confirmed", f"{selected['TotalConfirmed']:,}")
col2.metric("Deaths", f"{selected['TotalDeaths']:,}")
col3.metric("Recovered", f"{selected['TotalRecovered']:,}")

# Plot bar chart
fig = px.bar(
    x=["Confirmed", "Deaths", "Recovered"],
    y=[selected['TotalConfirmed'], selected['TotalDeaths'], selected['TotalRecovered']],
    labels={'x': 'Metric', 'y': 'Count'},
    title=f"Cases Breakdown in {country}",
    color=["Confirmed", "Deaths", "Recovered"]
)

st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Data Source: [covid19api.com](https://covid19api.com)")
