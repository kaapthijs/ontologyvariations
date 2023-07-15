import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('my_stats.xlsx')

# Get the unique versions
versions = df['Ontology'].unique()

# Increase the font size
plt.rcParams.update({'font.size': 22})

# Plotting the data
plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange', 'olive', 'purple']

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
    plt.plot(mean_reasoner_execution_time.index, mean_reasoner_execution_time, marker='o', color=colors[int(version[-1]) % len(colors)], label=f'{version[-1]}')

plt.xlabel('Trash Instances')
plt.ylabel('Time in s')
legend = plt.legend()
legend.get_frame().set_alpha(0)

plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
