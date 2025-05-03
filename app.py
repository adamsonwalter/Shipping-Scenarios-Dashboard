# app.py
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Asia Pacific Green Shipping 2045", layout="wide")
st.title("🚢 Green Shipping Scenarios in Asia Pacific by 2045")

# Scenario Selector
scenario = st.selectbox("Select a Scenario:", [
    "Coordinated Green Renaissance",
    "Polarized Greenwave",
    "Hydrogen Acceleration Bloc"
])

# Scenario Details
scenarios = {
    "Coordinated Green Renaissance": {
        "description": "Region-wide treaty, harmonized standards, dual-fuel deployment, strong public and investor support.",
        "emission_reduction": 70,
        "equity_score": 85,
        "resilience_score": 80
    },
    "Polarized Greenwave": {
        "description": "Fragmented coordination, bifurcated fuel systems, selective finance, tariff threats.",
        "emission_reduction": 50,
        "equity_score": 40,
        "resilience_score": 60
    },
    "Hydrogen Acceleration Bloc": {
        "description": "Tech-led retrofit boom, innovation-first but equity lags, private consortia drive progress.",
        "emission_reduction": 80,
        "equity_score": 55,
        "resilience_score": 70
    }
}

selected = scenarios[scenario]
st.markdown(f"### Description\n{selected['description']}")

# Impact Metrics
metrics_df = pd.DataFrame({
    'Metric': ['Emission Reduction (%)', 'Equity Score', 'Resilience Score'],
    'Value': [selected['emission_reduction'], selected['equity_score'], selected['resilience_score']]
})

chart = alt.Chart(metrics_df).mark_bar().encode(
    x=alt.X('Metric', sort=None),
    y='Value',
    color=alt.Color('Metric', scale=alt.Scale(scheme='tealblues'))
).properties(
    height=300, width=600
)

st.altair_chart(chart, use_container_width=True)

# Reflective Q&A Section
st.subheader("Reflective Questions")
if scenario == "Coordinated Green Renaissance":
    st.markdown("- How can mid-tier ports maintain competitiveness amid rapid corridor growth?")
elif scenario == "Polarized Greenwave":
    st.markdown("- What diplomatic strategies can re-knit fragmented decarbonization agendas?")
else:
    st.markdown("- Can innovation leadership coexist with inclusive policy frameworks?")
