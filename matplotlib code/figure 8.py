import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_excel('my_stats.xlsx')

# Group the data by version and calculate the mean of execution times
base_inferences = df.groupby('Ontology')['Ontology inferences'].mean()
inferences = df.groupby('Ontology')['Inferred Triples'].mean()


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(base_inferences.index, base_inferences, marker='o', label='Inferences before reasoner')
plt.plot(inferences.index, inferences, marker='o', label='Inferences after reasoner')

plt.xlabel('Version')
plt.ylabel('Execution Time')
plt.title('Mean inferences before reasoner vs mean inferences after reasoner')
plt.legend()
plt.xticks(rotation=90)
plt.grid(True)

plt.show()