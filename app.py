from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Uk affordability dashboard",
    layout="wide"
)

st.title("UK Housing Affordability Dashboard")

st.write(
    """
    This dashboard explores whether private rents have become less affordable
    across UK regions by comparing average monthly rent with median monthly pay.
    """
)

st.info(
    """
    Pay data refers to gross median monthly pay, not take-home pay after tax or deductions.
    Rent-to-pay ratio is calculated as average monthly rent divided by gross median monthly pay.
    """
)

# Load data

DATA_PATH = Path("data/processed/affordability_data.csv")

if not DATA_PATH.exists():
    st.error("The affordability data file could not be found.")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["time_period"] = pd.to_datetime(df["time_period"])

# Sidebar filters

st.sidebar.header("Filters")

regions = sorted(df["area_name"].unique())

selected_region = st.sidebar.selectbox(
    "Select a region:",
    regions,
    index=regions.index("United Kingdom") if "United Kingdom" in regions else 0
)

region_df = df[df["area_name"] == selected_region].copy()
region_df = region_df.sort_values("time_period")

# Latest values

latest_row = region_df.iloc[-1]
first_row = region_df.iloc[0]

rent_growth = (
    (latest_row["rental_price"] - first_row["rental_price"])
    / first_row["rental_price"]
) * 100

pay_growth = (
    (latest_row["median_monthly_pay"] - first_row["median_monthly_pay"])
    / first_row["median_monthly_pay"]
) * 100

st.subheader(f"Affordability overview: {selected_region}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Latest monthly rent",
    f"£{latest_row['rental_price']:,.0f}"
)

col2.metric(
    "Latest median monthly pay",
    f"£{latest_row['median_monthly_pay']:,.0f}"
)

col3.metric(
    "Rent as % of pay",
    f"{latest_row['rent_to_pay_percent']:.1f}%"
)

# Chart 1

st.subheader("Rent and pay over time")

fig_rent_pay = px.line(
    region_df,
    x="time_period",
    y=["rental_price", "median_monthly_pay"],
    title=f"Monthly rent and median pay in {selected_region}",
    labels={
        "time_period": "Date",
        "value": "£ per month",
        "variable": "Metric"
    }
)

st.plotly_chart(fig_rent_pay, use_container_width=True)

# Chart 2

st.subheader("Rent as a percentage of monthly median pay")

fig_affordability = px.line(
    region_df,
    x="time_period",
    y="rent_to_pay_percent",
    title=f"Rent to pay ratio in {selected_region}",
    labels={
        "time_period": "Date",
        "rent_to_pay_percent": "Rent as % of gross median monthly pay"
    }
)

st.plotly_chart(fig_affordability, use_container_width=True)

# Regional comparison
st.subheader("Latest regional comparison")

latest_date = df["time_period"].max()

latest_df = (
    df[df["time_period"] == latest_date]
    .sort_values("rent_to_pay_percent", ascending=False)
)

fig_latest = px.bar(
    latest_df,
    x="area_name",
    y="rent_to_pay_percent",
    title=f"Rent as % of median monthly pay by region, {latest_date.date()}",
    labels={
        "area_name": "Region",
        "rent_to_pay_percent": "Rent as % of gross median monthly pay"
    }
)

st.plotly_chart(fig_latest, use_container_width=True)

# Regional ranking
st.subheader("Latest regional ranking")

regional_ranking = latest_df[
    [
        "area_name",
        "rental_price",
        "median_monthly_pay",
        "rent_to_pay_percent"
    ]
].copy()

regional_ranking = regional_ranking.rename(columns = {
    "area_name": "Region",
    "rental_price": "Average monthly rent (£)",
    "median_monthly_pay": "Median monthly pay (£)",
    "rent_to_pay_percent": "Rent as % of pay"
})

regional_ranking["Average monthly rent (£)"] = regional_ranking["Average monthly rent (£)"].round(0)
regional_ranking["Median monthly pay (£)"] = regional_ranking["Median monthly pay (£)"].round(0)
regional_ranking["Rent as % of pay"] = regional_ranking["Rent as % of pay"].round(1)

st.dataframe(
    regional_ranking,
    use_container_width=True,
    hide_index=True
)

csv = df.to_csv(index=False)

st.download_button(
    label="Download affordability dataset",
    data=csv,
    file_name="affordability_data.csv",
    mime="text/csv"
)

# Methodology

st.subheader("Methodology")

st.write(
    """
    The analysis combines ONS private rent data with ONS PAYE Real Time Information
    median pay data. The key affordability metric is calculated as:

    **Rent-to-pay ratio = average monthly rent / gross median monthly pay × 100**

    This shows the share of gross median monthly pay represented by average monthly rent.
    """
)

# Summary
st.subheader("Summary")

st.write(
    f"""
    In {selected_region}, average monthly rent increased by **{rent_growth:.1f}%**
    over the period covered, while median monthly pay increased by **{pay_growth:.1f}%**.

    The latest rent-to-pay ratio is **{latest_row['rent_to_pay_percent']:.1f}%**,
    meaning average private rent is equivalent to this share of gross median monthly pay.
    """
)

