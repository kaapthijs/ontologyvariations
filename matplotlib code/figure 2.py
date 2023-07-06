import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
df = pd.read_excel('my_stats.xlsx')

# Extract the required columns
ontology_versions = df['Ontology']
ontology_subclasses = df['Ontology subclass axioms']
dataset_execution_time = df['Entire dataset execution time']

# Create a scatter plot for Ontology subclass axioms
plt.figure(figsize=(10, 6))
plt.bar(ontology_versions, ontology_subclasses, label='Ontology subclass axioms',)

# Create a scatter plot for Entire dataset execution time
#plt.plot(ontology_versions, dataset_execution_time, marker='o', label='Entire dataset execution time')

plt.xlabel('Version')
plt.ylabel('Value')
plt.title('Correlation between Ontology subclass axioms and Entire dataset execution time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.show()

# Create a scatter plot for Ontology subclass axioms
plt.figure(figsize=(10, 6))
#plt.plot(ontology_versions, ontology_subclasses, marker='o', label='Ontology subclass axioms',)

# Create a scatter plot for Entire dataset execution time
plt.plot(ontology_versions, dataset_execution_time, marker='o', linestyle='solid', label='Entire dataset execution time')

plt.xlabel('Version')
plt.ylabel('Value')
plt.title('Correlation between Ontology subclass axioms and Entire dataset execution time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.show()