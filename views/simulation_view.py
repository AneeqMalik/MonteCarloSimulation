import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simulation_View():
    st.title("Simulation of Delivery Delay")
    st.write("This is the Simulation of Monte Carlo Simulation of Delivery Delay page")
    # Function to calculate possible delay in delivery
    def calculate_delay(num_tasks, num_team_members):
        ratio = num_tasks / num_team_members
        if ratio > 2.5:
            return 10
        elif ratio > 2:
            return 7
        else:
            return 0

    # Monte Carlo simulation parameters
    num_simulations = 100000
    for _ in range(num_simulations):
        num_team_members = random.randint(st.session_state.dfData.min_team_members, st.session_state.dfData.max_team_members)
        delay = calculate_delay(st.session_state.dfData.num_tasks, num_team_members)
        st.session_state.dfData.delays.append(delay)
    
    # Calculate the mean of the delays
    mean_delay = np.mean(st.session_state.dfData.delays)

    # Calculate delay for specific input
    specific_team_members = 90
    specific_num_tasks = 100
    st.session_state.dfData.specific_delay = calculate_delay(specific_num_tasks, specific_team_members)

    # Calculate the percentile of the specific delay
    percentile = stats.percentileofscore(st.session_state.dfData.delays, st.session_state.dfData.specific_delay, kind='rank')

    st.write(f"Specific delay for {specific_team_members} team members and {specific_num_tasks} tasks: {st.session_state.dfData.specific_delay} days")
    st.write(f"Percentile of this delay in the simulation data: {percentile:.2f}%")

    # Plot the bar chart of the delays
    plt.hist(st.session_state.dfData.delays, bins=[0, 3, 10, 15], edgecolor='black', alpha=0.7, density=True)
    plt.xticks([0, 3, 10])
    plt.xlabel('Delay (Days)')
    plt.ylabel('Frequency')
    plt.title('Monte Carlo Simulation of Delivery Delay')

    # Plot the mean line
    plt.axvline(mean_delay, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_delay:.2f} days')

    # Overlay a bell curve (normal distribution)
    # We assume delays follow a normal distribution for visualization purposes
    mu, std = stats.norm.fit(st.session_state.dfData.delays)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label='Bell Curve (Normal Distribution)')

    plt.legend()
    st.pyplot(plt)