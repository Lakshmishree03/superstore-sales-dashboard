import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df

df = load_data()

st.title("Superstore Sales & Profit Dashboard")

# --- Sidebar filters ---
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Region", options=df['Region'].unique(), default=df['Region'].unique()
)
categories = st.sidebar.multiselect(
    "Category", options=df['Category'].unique(), default=df['Category'].unique()
)
date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(df['Order Date'].min(), df['Order Date'].max())
)

# Apply filters
mask = (
    df['Region'].isin(regions) &
    df['Category'].isin(categories) &
    (df['Order Date'] >= pd.to_datetime(date_range[0])) &
    (df['Order Date'] <= pd.to_datetime(date_range[1]))
)
filtered_df = df[mask]

# --- KPI row ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{filtered_df['Order ID'].nunique()}")

st.divider()

# --- Chart 1: Discount vs Profit ---
st.subheader("Discount vs Profit")
fig1 = px.scatter(
    filtered_df, x='Discount', y='Profit', color='Category',
    color_discrete_map={'Furniture': '#e74c3c', 'Office Supplies': '#2ecc71', 'Technology': '#3498db'},
    title="Higher discounts are associated with losses"
)
st.plotly_chart(fig1, use_container_width=True)

# --- Chart 2: Monthly Sales Trend ---
st.subheader("Sales by Calendar Month")
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
filtered_df['Month Name'] = filtered_df['Order Date'].dt.month_name()
monthly = filtered_df.groupby('Month Name')['Sales'].sum().reindex(month_order)
fig2 = px.bar(monthly, title="Total Sales by Calendar Month")
st.plotly_chart(fig2, use_container_width=True)

# --- Chart 3: Region performance ---
st.subheader("Sales & Profit by Region")
region_summary = filtered_df.groupby('Region')[['Sales','Profit']].sum().reset_index()
fig3 = px.bar(region_summary, x='Region', y=['Sales','Profit'], barmode='group')
st.plotly_chart(fig3, use_container_width=True)