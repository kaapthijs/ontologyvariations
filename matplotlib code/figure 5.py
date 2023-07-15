import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('my_stats.xlsx')

# Get the unique versions
versions = df['Ontology'].unique()

# Increase the font size
plt.rcParams.update({'font.size': 22})

# Iterate over each version and plot the data
    # Filter the data for the current version
version_df = df[df['Ontology'] == "version4"]

thrash_instances = version_df['Thrash instance count']
reasoner_execution_time = version_df['Reasoner Execution Time']
ontology_execution_time = version_df['Empty ontology execution time']

# Plotting the data
plt.figure(figsize=(10, 6))

mean_reasoner_execution_time = version_df.groupby('Thrash instance count')['Reasoner Execution Time'].mean()

plt.scatter(thrash_instances, reasoner_execution_time, marker='o', label='Timestamp')
plt.plot(thrash_instances, ontology_execution_time, marker='o', label='Base', color='red')
plt.plot(mean_reasoner_execution_time.index, mean_reasoner_execution_time, marker='o', label='Mean', color='olive')

plt.xlabel('Trash Instances')
plt.ylabel('Time in s')
plt.legend()

plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()  

