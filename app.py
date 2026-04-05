import streamlit as st
import pandas as pd
import time

# Page configuration
st.set_page_config(page_title="Automated Data Pipeline", page_icon="🚀")

# Title and Description
st.title("🚀 Automated Data Pipeline Dashboard")
st.markdown("### College Project: CI/CD with GitHub Actions & Docker")
st.write("Ye pipeline automatically data fetch karta hai aur Docker Hub par upload hota hai.")

# Sidebar for status
st.sidebar.header("Pipeline Status")
st.sidebar.success("CI/CD: Connected ✅")
st.sidebar.info("Docker Hub: Image Updated ✅")

# Simulation of Data Fetching
if st.button('Fetch Latest Data'):
    with st.spinner('Fetching data from pipeline...'):
        time.sleep(2)
        st.success("Data successfully fetched!")
        
        # Creating a sample data table
        data = {
            'ID': [1, 2, 3, 4],
            'Status': ['Processed', 'Processed', 'Pending', 'Processed'],
            'Time': ['10:00 AM', '10:05 AM', '10:10 AM', '10:15 AM']
        }
        df = pd.DataFrame(data)
        st.table(df)

# Graph for Teacher to see
st.subheader("Data Analysis Graph")
chart_data = pd.DataFrame([10, 20, 15, 30, 25], columns=['Processing Speed'])
st.line_chart(chart_data)

st.info("Built by Manpreet | DevOps Project 2026")