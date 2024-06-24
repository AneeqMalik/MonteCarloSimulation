import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import streamlit as st

def delivery_acceptedView():
    st.title("Deliverables Accepted")
    st.write("The number of accepted deliverables can impact customer retention rates. ")
    # Specific number of accepted deliverables estimate
    specific_accepted = st.number_input('Enter Specific number of accepted deliverables estimate', min_value=1, value=7)

    # Parameters for binomial distribution
    num_trials = 10  # Total number of deliverables submitted
    success_probability = 0.7  # Probability of acceptance for each deliverable
    num_simulations = 100000  # Number of simulations

    # Simulate the number of accepted deliverables using a binomial distribution
    accepted_deliverables = np.random.binomial(num_trials, success_probability, num_simulations)

    # Visualize the distribution of accepted deliverables
    plt.hist(accepted_deliverables, bins=np.arange(num_trials+2)-0.5, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Number of Accepted Deliverables')
    plt.ylabel('Frequency')
    plt.title('Distribution of Accepted Deliverables')

    # Plot the mean line
    mean_accepted = np.mean(accepted_deliverables)
    plt.axvline(mean_accepted, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_accepted:.2f} Deliverables')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Calculate and visualize the Probability Mass Function (PMF)
    x = np.arange(0, num_trials + 1)
    pmf = stats.binom.pmf(x, num_trials, success_probability)

    plt.stem(x, pmf, 'k', basefmt=" ")
    plt.xlabel('Number of Accepted Deliverables')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of Accepted Deliverables')
    st.pyplot(plt)
    plt.clf()

    # Parameters for binomial distribution
    num_trials = 10  # Total number of deliverables submitted
    success_probability = 0.7  # Probability of acceptance for each deliverable
    num_simulations = 100000  # Number of simulations

    # Function to determine customer retention based on the number of accepted deliverables
    def determine_customer_retention(num_accepted):
        if num_accepted > 4:
            return 0.2  # 20% retention
        elif num_accepted > 8:
            return 0.75  # 75% retention
        else:
            return 1.0  # 100% retention

    # Simulate the number of accepted deliverables using a binomial distribution
    accepted_deliverables = np.random.binomial(num_trials, success_probability, num_simulations)

    # Determine customer retention probabilities based on accepted deliverables
    retention_probabilities = np.array([determine_customer_retention(num) for num in accepted_deliverables])

    # Visualize the distribution of accepted deliverables
    plt.hist(accepted_deliverables, bins=np.arange(num_trials+2)-0.5, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Number of Accepted Deliverables')
    plt.ylabel('Frequency')
    plt.title('Distribution of Accepted Deliverables')

    # Plot the mean line
    mean_accepted = np.mean(accepted_deliverables)
    plt.axvline(mean_accepted, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_accepted:.2f} Deliverables')
    plt.legend()
    st.pyplot(plt)
    plt.clf()

    # Calculate and visualize the Probability Mass Function (PMF)
    x = np.arange(0, num_trials + 1)
    pmf = stats.binom.pmf(x, num_trials, success_probability)

    plt.stem(x, pmf, 'k', basefmt=" ")
    plt.xlabel('Number of Accepted Deliverables')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of Accepted Deliverables')
    st.pyplot(plt)
    plt.clf()

    # Visualize the distribution of retention probabilities
    plt.hist(retention_probabilities, bins=[0, 0.2, 0.75, 1], edgecolor='black', alpha=0.7, density=True)
    plt.xlabel('Customer Retention Probability')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer Retention Probabilities')
    plt.xticks([0.2, 0.75, 1], ['20%', '75%', '100%'])
    st.pyplot(plt)
    plt.clf()

   
    # Calculate the percentile of the specific number of accepted deliverables
    percentile = stats.percentileofscore(accepted_deliverables, specific_accepted, kind='rank')

    st.write(f"Specific number of accepted deliverables estimate: {specific_accepted}")
    st.write(f"Percentile of this estimate in the simulation data: {percentile:.2f}%")

    # Specific number of accepted deliverables and corresponding retention probability
    specific_retention_probability = determine_customer_retention(specific_accepted)

    st.write(f"Specific number of accepted deliverables: {specific_accepted}")
    st.write(f"Customer retention probability for this number of accepted deliverables: {specific_retention_probability * 100}%")
