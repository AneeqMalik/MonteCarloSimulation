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



# Initialize session state if it doesn't exist
if 'dfData' not in st.session_state:
    st.session_state.dfData = Data()


with st.sidebar:
    selected = option_menu(
    menu_title = "Monte Carlo Simulation",
    options = ["HISTORICAL DATA GATHERING","Simulation of Delivery Delay","Evaluation","Storage"],
    icons = ["database-up","activity","person-arms-up","arrow-repeat","envelope"],
    menu_icon = "radioactive",
    default_index = 0,
)

if selected == "HISTORICAL DATA GATHERING":
    histogram_View()

elif selected == "Simulation of Delivery Delay":
    simulation_View()

elif selected == "Evaluation":
    evaluation_View()


        

