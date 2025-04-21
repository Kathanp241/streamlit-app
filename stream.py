import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🦠 COVID-19 Live Dashboard")

# Load data from API
@st.cache_data(ttl=3600)
def load_data():
    try:
        response = requests.get("https://api.covid19api.com/summary")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error("Failed to fetch data from the API. Please try again later.")
        return None

data = load_data()

if data and "Countries" in data:
    countries_df = pd.DataFrame(data['Countries'])

    # Country selector
    country_list = countries_df['Country'].sort_values().tolist()
    country = st.selectbox("🌍 Select a country", country_list)

    # Get selected country's data
    selected = countries_df[countries_df['Country'] == country].squeeze()

    st.subheader(f"📊 COVID-19 Statistics for {country}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Confirmed", f"{selected['TotalConfirmed']:,}")
    col2.metric("Total Deaths", f"{selected['TotalDeaths']:,}")
    col3.metric("Total Recovered", f"{selected['TotalRecovered']:,}")

    # Bar chart using Plotly
    fig = px.bar(
        x=["Confirmed", "Deaths", "Recovered"],
        y=[selected['TotalConfirmed'], selected['TotalDeaths'], selected['TotalRecovered']],
        labels={"x": "Metric", "y": "Number of Cases"},
        title=f"COVID-19 Case Breakdown in {country}",
        color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown("📌 Data Source: [covid19api.com](https://covid19api.com) | Made with ❤️ using Streamlit")

else:
    st.warning("No data available at the moment.")

