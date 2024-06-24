import streamlit as st
import pandas as pd
import numpy as np
import streamlit_option_menu
import matplotlib.pyplot as plt
import time
import random
from streamlit_option_menu import option_menu
from data.data import Data
from scipy import stats
from views.histogram_view import histogram_View
from views.simulation_view import simulation_View
from views.evaluation_view import evaluation_View
from views.delay_tasks_view import delay_Tasks_View
from views.change_request_view import change_request_View
from views.delivery_accepted_view import delivery_acceptedView



# Initialize session state if it doesn't exist
if 'dfData' not in st.session_state:
    st.session_state.dfData = Data()


with st.sidebar:
    selected = option_menu(
    menu_title = "Monte Carlo Simulation",
    options = ["HISTORICAL DATA GATHERING","Simulation of Delivery Delay","Evaluation","Delay Between Tasks", "Change Request Received", "Deliverables Accepted"],
    icons = ["database-up","activity","person-arms-up","arrow-repeat","currency-exchange", "truck"],
    menu_icon = "radioactive",
    default_index = 0,
)

if selected == "HISTORICAL DATA GATHERING":
    histogram_View()

elif selected == "Simulation of Delivery Delay":
    if st.session_state.dfData.mean_cost == None:
        st.write("Data is empty. Please gather historical data first.")
    else:
        simulation_View()

elif selected == "Evaluation":
    if st.session_state.dfData.mean_cost == None:
        st.write("Data is empty. Please gather historical data first.")
    else:
        evaluation_View()

elif selected == "Delay Between Tasks":
    if st.session_state.dfData.mean_interval == None:
        st.write("Data is empty. Please gather historical data first.")
    else:
        delay_Tasks_View()

elif selected == "Change Request Received":
    if st.session_state.dfData.mean_interval == None:
        st.write("Data is empty. Please gather historical data first.")
    else:
        change_request_View()

elif selected == "Deliverables Accepted":
    if st.session_state.dfData.mean_interval == None:
        st.write("Data is empty. Please gather historical data first.")
    else:
        delivery_acceptedView()


        

