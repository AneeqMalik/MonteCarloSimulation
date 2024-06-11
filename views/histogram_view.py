import streamlit as st
import pandas as pd

def histogram_View():
    st.title("Historical Data Gathering")
    st.write("This is the Historical Data Gathering page")
    # Upload the CSV file
    uploaded_file = st.file_uploader("Choose a historical data file", type="csv")
    if uploaded_file is not None and uploaded_file.type == "text/csv":
        data = pd.read_csv(uploaded_file)
        st.write(data)
        df = pd.DataFrame(data)
        st.session_state.dfData.min_team_members=df['team_members'].min()
        st.session_state.dfData.max_team_members=df['team_members'].max()
        st.session_state.dfData.num_tasks=df['number_of_tasks_per_team'].mean()
        st.session_state.dfData.mean_cost = df['project_cost'].mean()
        st.session_state.dfData.std_dev_cost = df['project_cost'].std()
        st.session_state.dfData.min_usage = df['resource_usage'].min()
        st.session_state.dfData.most_likely_usage = df['resource_usage'].mode()[0]
        st.session_state.dfData.max_usage = df['resource_usage'].max()
        st.session_state.dfData.mean_interval = df['time_between_phases'].mean()
        st.session_state.dfData.average_requests_per_day = df['change_requests'].mean()
        st.session_state.dfData.project_duration = df['project_duration'].mean()