import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import streamlit as st

def delay_Tasks_View():
    num_simulations = 100000  # Number of simulations

    # Simulate time intervals using an exponential distribution
    time_intervals = np.random.exponential(st.session_state.dfData.mean_interval, num_simulations)

    # Visualize the distribution of time intervals
    plt.hist(time_intervals, bins=50, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Time Interval (Days)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Time Intervals Between Task Completions')

    # Plot the mean line
    mean_usage = np.mean(time_intervals)
    plt.axvline(mean_usage, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_usage:.2f} Days')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Calculate and visualize the Probability Density Function (PDF)
    x = np.linspace(0, np.max(time_intervals), 1000)
    pdf = stats.expon.pdf(x, scale=st.session_state.dfData.mean_interval)

    plt.plot(x, pdf, 'k', linewidth=2, label='Exponential Distribution (PDF)')
    plt.xlabel('Time Interval (Days)')
    plt.ylabel('Probability Density')
    plt.title('Probability Density Function of Time Intervals')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Simulate time intervals using an exponential distribution
    time_intervals = np.random.exponential(st.session_state.dfData.mean_interval, num_simulations)

    # Apply dissatisfaction levels based on time intervals
    dissatisfaction_levels = np.array([determine_dissatisfaction(ti) for ti in time_intervals])

    # Visualize the distribution of dissatisfaction levels
    plt.hist(dissatisfaction_levels, bins=[0, 0.2, 0.5, 0.8, 1], edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Dissatisfaction Level')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer Dissatisfaction Levels')
    plt.xticks([0.2, 0.5, 0.8], ['20%', '50%', '80%'])
    st.pyplot(plt)
    plt.clf()

    specific_time_interval = st.number_input("Enter a specific time interval", min_value=0, value=7)

    # Calculate the percentile of the specific time interval
    percentile = stats.percentileofscore(time_intervals, specific_time_interval, kind='rank')

    st.write(f"Specific time interval estimate: {specific_time_interval} Days")
    st.write(f"Percentile of this estimate in the simulation data: {percentile:.2f}%")

    # Specific time interval and corresponding dissatisfaction
    specific_dissatisfaction = determine_dissatisfaction(specific_time_interval)

    st.write(f"Specific time interval: {specific_time_interval} Days")
    st.write(f"Customer dissatisfaction for this time interval: {specific_dissatisfaction * 100}%")

# Function to determine customer dissatisfaction based on time interval
def determine_dissatisfaction(time_interval):
    if time_interval > 5:
        return 0.8  # 80% dissatisfaction
    elif time_interval > 2:
        return 0.5  # 50% dissatisfaction
    else:
        return 0.2  # 20% dissatisfaction