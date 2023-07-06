import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_excel('my_stats.xlsx')

# Group the data by version and calculate the mean of execution times
mean_empty_time = df.groupby('Ontology')['Empty ontology execution time'].mean()
mean_reasoner_time = df.groupby('Ontology')['Reasoner Execution Time'].mean()


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(mean_empty_time.index, mean_empty_time, marker='o', label='Mean Empty Ontology Time')
plt.plot(mean_reasoner_time.index, mean_reasoner_time, marker='o', label='Mean Reasoner Time')

plt.xlabel('Version')
plt.ylabel('Execution Time')
plt.title('Mean Execution Time for Empty Ontology and Reasoner by Version')
plt.legend()
plt.xticks(rotation=90)
plt.grid(True)

plt.show()