import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DevOps Data Pipeline", layout="wide")

# Sidebar - Project Info
st.sidebar.title("📌 Project Details")
st.sidebar.info("Developer: Manpreet Singh\nBranch: B.Tech Final Year")

st.title("📊 Automated Data Pipeline Dashboard")
st.markdown("---")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file (e.g., test_data.csv)", type="csv")

if uploaded_file is not None:
    # Load Data
    df = pd.read_csv(uploaded_file)
    
    # 1. Key Metrics (Highlights)
    st.subheader("💡 Key Highlights")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    total_sales = df['Sales'].sum() if 'Sales' in df.columns else 0
    total_items = len(df)
    
    kpi1.metric("Total Revenue", f"₹{total_sales:,}")
    kpi2.metric("Orders Count", total_items)
    kpi3.metric("Status", "Pipeline Active ✅")

    st.markdown("---")

    # 2. Charts (Visuals)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Sales by Product")
        if 'Product' in df.columns and 'Sales' in df.columns:
            fig_bar = px.bar(df, x='Product', y='Sales', color='Product', text_auto=True)
            st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("🥧 Order Status Distribution")
        if 'Status' in df.columns:
            fig_pie = px.pie(df, names='Status', hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)

    # 3. Data Table
    st.subheader("📄 Raw Data Preview")
    st.dataframe(df, use_container_width=True)

else:
    st.warning("👈 Please upload the 'test_data.csv' file to see the magic!")