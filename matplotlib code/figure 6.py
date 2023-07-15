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
    inferred_triples = version_df['Inferred Triples']
    reasoner_execution_time = version_df['Reasoner Execution Time']
    ontology_execution_time = version_df['Empty ontology execution time']

    # Calculate the mean reasoner execution time for the current version
    mean_reasoner_execution_time = version_df.groupby('Inferred Triples')['Reasoner Execution Time'].mean()

    # Plot the data for the current version
    #plt.scatter(thrash_instances, reasoner_execution_time, marker='o', label=f'{version} - Reasoner Execution Time')
    #plt.plot(thrash_instances, ontology_execution_time, marker='o', label=f'{version} - Empty ontology execution time')
    plt.scatter(mean_reasoner_execution_time.index, mean_reasoner_execution_time, marker='o', color=colors[int(version[-1]) % len(colors)], label=f'{version[-1]}')

plt.xlabel('Inferred Triples')
plt.ylabel('Time in s')
plt.legend()

plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
