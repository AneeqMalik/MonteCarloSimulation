import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def evaluation_View():
    tab1, tab2, tab3 = st.tabs(["HUMAN PERFORMANCE EVALUATION", "Resource Usage Evaluation", "Project Cost Evaluation"])
    
    with tab1:
        st.title("Human Performance Evaluation")
        st.write("This is the Human Performance Evaluation page")
        # Calculate delay for specific input
        specific_team_members = st.number_input('Enter specific team members', min_value=1, value=90)
        specific_num_tasks = st.number_input('Enter specific number of tasks', min_value=1, value=100)

        num_samples = 100000
        
        # Randomly determine the number of team members within the given range
        team_size = np.random.randint(st.session_state.dfData.min_team_members, st.session_state.dfData.max_team_members + 1, num_samples)
        pdf = np.ones_like(team_size) / (st.session_state.dfData.max_team_members - st.session_state.dfData.min_team_members)
        
        # Plot the probability density function
        plt.figure(figsize=(10, 6))
        plt.plot(team_size, pdf, label='PDF')
        
        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.title('Probability Density Function of Uniform Distribution')
        plt.legend()
        plt.grid(True)
        
        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.clf()
        
        # Visualize the distribution of team sizes (PDF)
        plt.figure(figsize=(10, 6))
        plt.hist(team_size, bins=range(st.session_state.dfData.min_team_members, st.session_state.dfData.max_team_members + 2), edgecolor='black', density=True)
        plt.xlabel('Number of Team Members')
        plt.ylabel('Probability Density')
        plt.title('Distribution of Team Sizes (PDF)')
        
        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.clf()

        # Function to calculate possible delay in delivery
        def calculate_delay(num_tasks, num_team_members):
            ratio = num_tasks / num_team_members
            if ratio > 2.5:
                return 10
            elif ratio > 2:
                return 7
            else:
                return 0
        
        specific_delay = calculate_delay(specific_num_tasks, specific_team_members)

        # Calculate the percentile of the specific delay
        percentile = stats.percentileofscore(st.session_state.dfData.delays, specific_delay, kind='rank')

        st.write(f"Specific delay for {specific_team_members} team members and {specific_num_tasks} tasks: {specific_delay} days")
        st.write(f"Percentile of this delay in the simulation data: {percentile:.2f}%")
    
    with tab2:
        st.title("Resource Usage Evaluation")
        st.write("This is the Resource Usage Evaluation page")

        # Function to determine resource usage increase based on delay
        def determine_resource_increase(delay):
            if delay > 8:
                return 0.5  # 50% increase
            elif delay > 5:
                return 0.2  # 20% increase
            else:
                return 0  # No increase

        num_simulations = 100000  # Number of simulations

        specific_resource_usage = st.number_input('Enter specific resource usage', min_value=1, value=75)

        # Simulate resource usage estimates using a triangular distribution
        resource_usage = np.random.triangular(st.session_state.dfData.min_usage, st.session_state.dfData.most_likely_usage, st.session_state.dfData.max_usage, num_simulations)

        # Visualize the distribution of resource usage
        plt.hist(resource_usage, bins=50, edgecolor='black', alpha=0.7, density=True)
        plt.xlabel('Resource Usage')
        plt.ylabel('Frequency')
        plt.title('Distribution of Resource Usage Estimates')

        # Plot the mean line
        mean_usage = np.mean(resource_usage)
        plt.axvline(mean_usage, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_usage:.2f} Units')
        plt.legend()

        # Display the plot in Streamlit
        st.pyplot(plt)

        plt.clf()  # Clear the previous plot

        # Calculate and visualize the Probability Density Function (PDF)
        x = np.linspace(min(resource_usage), max(resource_usage), 1000)
        pdf = stats.triang.pdf(x, (st.session_state.dfData.most_likely_usage - st.session_state.dfData.min_usage) / (st.session_state.dfData.max_usage - st.session_state.dfData.min_usage), loc=st.session_state.dfData.min_usage, scale=st.session_state.dfData.max_usage - st.session_state.dfData.min_usage)

        plt.plot(x, pdf, 'k', linewidth=2, label='Triangular Distribution (PDF)')
        plt.xlabel('Resource Usage')
        plt.ylabel('Probability Density')
        plt.title('Probability Density Function of Resource Usage Estimates')
        plt.legend()

        # Specific resource usage estimate
        resource_increase_factor = determine_resource_increase(st.session_state.dfData.specific_delay)
        specific_resource_usage *= (1 + resource_increase_factor)

        # Calculate the percentile of the specific resource usage
        percentile = stats.percentileofscore(resource_usage, specific_resource_usage, kind='rank')

        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.clf()  # Clear the previous plot

        # Function to determine resource usage increase based on delay
        def determine_resource_increase(delay):
            if delay > 8:
                return 0.5  # 50% increase
            elif delay > 5:
                return 0.2  # 20% increase
            else:
                return 0  # No increase

        # Simulate resource usage estimates using a triangular distribution
        resource_usage = np.random.triangular(st.session_state.dfData.min_usage, st.session_state.dfData.most_likely_usage, st.session_state.dfData.max_usage, num_simulations)

        # Apply resource increases based on delays
        for i in range(num_simulations):
            resource_increase_factor = determine_resource_increase(st.session_state.dfData.delays[i])
            resource_usage[i] *= (1 + resource_increase_factor)

        # Visualize the distribution of resource usage
        plt.hist(resource_usage, bins=50, edgecolor='black', alpha=0.7, density=True)
        plt.xlabel('Resource Usage')
        plt.ylabel('Frequency')
        plt.title('Distribution of Resource Usage Estimates')

        # Plot the mean line
        mean_usage = np.mean(resource_usage)
        plt.axvline(mean_usage, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_usage:.2f} Units')
        plt.legend()
        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.clf()

        # Calculate and visualize the Probability Density Function (PDF)
        x = np.linspace(min(resource_usage), max(resource_usage), 1000)
        pdf = stats.triang.pdf(x, (st.session_state.dfData.most_likely_usage - st.session_state.dfData.min_usage) / (st.session_state.dfData.max_usage - st.session_state.dfData.min_usage), loc=st.session_state.dfData.min_usage, scale=st.session_state.dfData.max_usage - st.session_state.dfData.min_usage)

        plt.plot(x, pdf, 'k', linewidth=2, label='Triangular Distribution (PDF)')
        plt.xlabel('Resource Usage')
        plt.ylabel('Probability Density')
        plt.title('Probability Density Function of Resource Usage Estimates')
        plt.legend()

        # Display the plot in Streamlit
        st.pyplot(plt)
        plt.clf()

        # Specific resource usage estimate
        resource_increase_factor = determine_resource_increase(st.session_state.dfData.specific_delay)
        specific_resource_usage *= (1 + resource_increase_factor)

        # Calculate the percentile of the specific resource usage
        percentile = stats.percentileofscore(resource_usage, specific_resource_usage, kind='rank')

        st.write(f"Specific resource usage estimate: {specific_resource_usage} Units")
        st.write(f"Percentile of this estimate in the simulation data: {percentile:.2f}%")

    with tab3:
        st.title("Project Cost Evaluation")
        st.write("This is the Project Cost Evaluation page")
        # Parameters
        mean_cost = 50000  # Mean project cost
        std_dev_cost = 10000  # Standard deviation of project cost
        num_simulations = 100000  # Number of simulations

        # Simulate project cost estimates using a normal distribution
        project_costs = np.random.normal(mean_cost, std_dev_cost, num_simulations)

        # Visualize the distribution of project costs
        plt.hist(project_costs, bins=50, edgecolor='black', alpha=0.7, density=True)
        plt.xlabel('Project Cost')
        plt.ylabel('Frequency')
        plt.title('Distribution of Project Cost Estimates')

        # Plot the mean line
        plt.axvline(mean_cost, color='r', linestyle='dashed', linewidth=2, label=f'Mean = ${mean_cost}')
        plt.legend()
        # plt.show()
        st.pyplot(plt)
        plt.clf()

        # Calculate and visualize the Probability Density Function (PDF)
        x = np.linspace(min(project_costs), max(project_costs), 1000)
        pdf = stats.norm.pdf(x, mean_cost, std_dev_cost)

        plt.plot(x, pdf, 'k', linewidth=2, label='Normal Distribution (PDF)')
        plt.xlabel('Project Cost')
        plt.ylabel('Probability Density')
        plt.title('Probability Density Function of Project Cost Estimates')
        plt.legend()
        # plt.show()
        st.pyplot(plt)
        plt.clf()

        #Resource Calculation missing
        # Function to determine cost increase based on delay
        def determine_cost_increase(delay):
            if delay > 8:
                return 0.5  # 50% increase
            elif delay > 5:
                return 0.2  # 20% increase
            else:
                return 0  # No increase

        # Simulate project cost estimates using a normal distribution
        project_costs = np.random.normal(mean_cost, std_dev_cost, num_simulations)

        # Apply cost increases based on delays
        for i in range(num_simulations):
            cost_increase_factor = determine_cost_increase(st.session_state.dfData.delays[i])
            project_costs[i] *= (1 + cost_increase_factor)

        mean_cost = np.mean(project_costs)
        # Visualize the distribution of project costs
        plt.hist(project_costs, bins=50, edgecolor='black', alpha=0.7, density=True)
        plt.xlabel('Project Cost')
        plt.ylabel('Frequency')
        plt.title('Distribution of Project Cost Estimates')

        # Plot the mean line
        plt.axvline(mean_cost, color='r', linestyle='dashed', linewidth=2, label=f'Mean = ${mean_cost}')
        plt.legend()
        plt.show()
        st.pyplot(plt)
        plt.clf()

        # Calculate and visualize the Probability Density Function (PDF)
        x = np.linspace(min(project_costs), max(project_costs), 1000)
        pdf = stats.norm.pdf(x, mean_cost, std_dev_cost)

        plt.plot(x, pdf, 'k', linewidth=2, label='Normal Distribution (PDF)')
        plt.xlabel('Project Cost')
        plt.ylabel('Probability Density')
        plt.title('Probability Density Function of Project Cost Estimates')
        plt.legend()
        plt.show()
        st.pyplot(plt)
        plt.clf()
        # Specific project cost estimate
        specific_project_cost = 55000
        cost_increase_factor = determine_cost_increase(st.session_state.dfData.specific_delay)
        specific_project_cost*= (1 + cost_increase_factor)

        # Calculate the percentile of the specific project cost
        percentile = stats.percentileofscore(project_costs, specific_project_cost, kind='rank')

        st.write(f"Specific project cost estimate: ${specific_project_cost}")
        st.write(f"Percentile of this estimate in the simulation data: {percentile:.2f}%")