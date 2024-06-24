import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import streamlit as st


def change_request_View():
    st.title("Change Request Received")
    st.write("Change requests are common in project management and can affect project estimations. ")
    num_simulations = 100000  # Number of simulations4
    specific_requests = st.number_input('Enter Specific Requests', min_value=1, value=5)
    project_duration = st.number_input('Enter Project Duration', min_value=1, value=20)

    # Simulate the number of change requests using a Poisson distribution
    change_requests = np.random.poisson(st.session_state.dfData.average_requests_per_day * st.session_state.dfData.project_duration, num_simulations)

    # Visualize the distribution of change requests
    plt.hist(change_requests, bins=50, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Number of Change Requests')
    plt.ylabel('Frequency')
    plt.title('Distribution of Change Requests During Project Phase')

    # Plot the mean line
    mean_requests = np.mean(change_requests)
    plt.axvline(mean_requests, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_requests:.2f} Requests')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Calculate and visualize the Probability Mass Function (PMF)
    x = np.arange(0, np.max(change_requests) + 1)
    pmf = stats.poisson.pmf(x,  st.session_state.dfData.average_requests_per_day *  st.session_state.dfData.project_duration)

    plt.stem(x, pmf, 'k', basefmt=" ")
    plt.xlabel('Number of Change Requests')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of Change Requests')
    st.pyplot(plt)
    plt.clf()


    num_simulations = 100000  # Number of simulations

    # Function to determine the probability of affecting project estimations
    def affect_project_estimations(requests):
        if requests < 15:
            return 0.5  # 50% chance
        elif requests < 25:
            return 0.3  # 30% chance
        else:
            return 0.9  # 90% chance

    # Simulate the number of change requests using a Poisson distribution
    change_requests = np.random.poisson(st.session_state.dfData.average_requests_per_day * st.session_state.dfData.project_duration, num_simulations)

    # Determine the probabilities of affecting project estimations
    affect_probabilities = np.array([affect_project_estimations(req) for req in change_requests])

    # Visualize the distribution of change requests
    plt.hist(change_requests, bins=50, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Number of Change Requests')
    plt.ylabel('Frequency')
    plt.title('Distribution of Change Requests During Project Phase')

    # Plot the mean line
    mean_requests = np.mean(change_requests)
    plt.axvline(mean_requests, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_requests:.2f} Requests')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Calculate and visualize the Probability Mass Function (PMF)
    x = np.arange(0, np.max(change_requests) + 1)
    pmf = stats.poisson.pmf(x, st.session_state.dfData.average_requests_per_day * st.session_state.dfData.project_duration)

    plt.stem(x, pmf, 'k', basefmt=" ")
    plt.xlabel('Number of Change Requests')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of Change Requests')
    st.pyplot(plt)
    plt.clf()

    # Visualize the distribution of affect probabilities
    plt.hist(affect_probabilities, bins=[0, 0.3, 0.5, 0.9, 1], edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Probability of Affecting Project Estimations')
    plt.ylabel('Frequency')
    plt.title('Distribution of Affect Probabilities')
    plt.xticks([0.3, 0.5, 0.9], ['30%', '50%', '90%'])
    st.pyplot(plt)
    plt.clf()

    
    change_requests = specific_requests * project_duration
    # Specific number of change requests and corresponding affect probability
    specific_affect_probability = affect_project_estimations(change_requests)

    st.write(f"Specific number of change requests: {specific_requests} Requests")
    st.write(f"Probability of affecting project estimations for this number of requests: {specific_affect_probability * 100}%")