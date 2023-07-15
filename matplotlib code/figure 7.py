import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_excel('my_stats.xlsx')

# Group the data by version and calculate the mean of execution times
mean_empty_time = df.groupby('Ontology')['Empty ontology execution time'].mean()
mean_reasoner_time = df.groupby('Ontology')['Reasoner Execution Time'].mean()

plt.rcParams.update({'font.size': 22})

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(mean_empty_time.index, mean_empty_time, marker='o', label='Empty Ontology Execution Time')
plt.plot(mean_reasoner_time.index, mean_reasoner_time, marker='o', label='Mean Timestamp Execution Time')

plt.xticks(range(len(mean_empty_time.index)), mean_empty_time.index.astype(str).str[-1])

plt.xlabel('Version')
plt.ylabel('Execution Time')
legend = plt.legend()
legend.get_frame().set_alpha(0)
plt.xticks()
plt.grid(True)
plt.tight_layout()
plt.show()