import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('my_stats.xlsx')

# Get the unique versions
versions = df['Ontology'].unique()

# Plotting the data
plt.figure(figsize=(10, 6))

# Iterate over each version and plot the data
for version in versions:
    # Filter the data for the current version
    version_df = df[df['Ontology'] == version]

    # Extract the relevant columns from the DataFrame
    thrash_instances = version_df['Thrash instance count']
    reasoner_execution_time = version_df['Reasoner Execution Time']
    ontology_execution_time = version_df['Empty ontology execution time']

    # Calculate the mean reasoner execution time for the current version
    mean_reasoner_execution_time = version_df.groupby('Thrash instance count')['Reasoner Execution Time'].mean()

    # Plot the data for the current version
    #plt.scatter(thrash_instances, reasoner_execution_time, marker='o', label=f'{version} - Reasoner Execution Time')
    #plt.plot(thrash_instances, ontology_execution_time, marker='o', label=f'{version} - Empty ontology execution time')
    plt.plot(mean_reasoner_execution_time.index, mean_reasoner_execution_time, marker='o', label=f'{version} - Mean Reasoner Execution Time')

plt.xlabel('Thrash instance count')
plt.ylabel('Time in seconds')
plt.title('Reasoner execution time')
plt.legend()

plt.grid(True)

# Display the plot
plt.show()
