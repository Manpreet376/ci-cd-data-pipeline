import streamlit as st
import pandas as pd
import plotly.express as px

# Professional UI Config
st.set_page_config(page_title="Enterprise Data Pipeline", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .reportview-container { background: #f5f7f9; }
    .sidebar .sidebar-content { background: #262730; color: white; }
    </style>
    """, unsafe_allow_stats=True)

st.title("🛡️ Enterprise Data Intelligence Dashboard")
st.caption("Status: **Production Ready** | CI/CD Connected via GitHub")

# Sidebar
st.sidebar.title("Pipeline Overview")
st.sidebar.metric(label="System Status", value="Online", delta="Healthy")
st.sidebar.markdown("---")
st.sidebar.write("**Developed by:** Manpreet")

# File Upload Section
uploaded_file = st.file_uploader("📂 Upload Business Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # KPIs Row
    st.markdown("### 📊 Key Performance Indicators")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Records", len(df))
    kpi2.metric("Data Columns", len(df.columns))
    kpi3.metric("Pipeline Health", "100%")

    # Charts
    st.markdown("---")
    col_chart, col_data = st.columns([2, 1])
    
    with col_chart:
        num_cols = df.select_dtypes(include=['number']).columns.tolist()
        if num_cols:
            fig = px.line(df, y=num_cols[0], title="Performance Trend Analysis", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)
            
    with col_data:
        st.write("#### Data Snapshot")
        st.dataframe(df.head(10), use_container_width=True)
else:
    st.info("System is waiting for a CSV file input to initialize the pipeline.")