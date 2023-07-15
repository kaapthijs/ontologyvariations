import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_excel('my_stats.xlsx')

# Group the data by version and calculate the mean of execution times
base_inferences = df.groupby('Ontology')['Ontology inferences'].mean()
inferences = df.groupby('Ontology')['Inferred Triples'].mean()

plt.rcParams.update({'font.size': 22})

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(base_inferences.index, base_inferences, marker='o', label='Inferences before reasoner')
plt.plot(inferences.index, inferences, marker='o', label='Inferences after reasoner')

plt.xticks(range(len(base_inferences.index)), base_inferences.index.astype(str).str[-1])

plt.xlabel('Version')
plt.ylabel('Execution Time')
legend = plt.legend()
legend.get_frame().set_alpha(0)
plt.xticks()
plt.grid(True)
plt.tight_layout()
plt.show()