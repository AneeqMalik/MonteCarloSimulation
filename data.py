import pandas as pd

# Create a dictionary with the data
data = {
    'project_name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
    'team_members': [5, 10, 7,30, 25],
    'number_of_tasks_per_team': [20, 35, 25, 60, 50],
    'project_cost': [100000, 200000, 150000, 400000, 350000],
    'resource_usage': [20, 100, 50,50,50],
    'time_between_phases': [2, 3, 2,4,5],  # in days
    'change_requests': [5, 10, 7, 1 ,2],
    'project_duration': [12, 18, 14,20,10]  # in months
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)