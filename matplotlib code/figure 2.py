import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('my_stats.xlsx')

# Extract the required columns
ontology_versions = df['Ontology'].astype(str).str[-1]
ontology_subclasses = df['Ontology subclass axioms']
dataset_execution_time = df['Entire dataset execution time']

# Increase the font size
plt.rcParams.update({'font.size': 22})

# Create a scatter plot for Ontology subclass axioms
plt.figure(figsize=(10, 6))
plt.bar(ontology_versions, ontology_subclasses, label='Ontology subclass axioms',)

plt.xlabel('Version')
plt.ylabel('Subclass Axiom Amount')
plt.xticks()
plt.grid(True)
plt.tight_layout()
plt.show()