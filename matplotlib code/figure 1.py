import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('my_stats.xlsx')

# Extract the required columns
ontology_versions = df['Ontology'].astype(str).str[-1]
ontology_inferences = df['Ontology inferences']
ontology_subclasses = df['Ontology subclass axioms']
ontology_thrash_instances = df['Ontology Thrash instance count']
ontology_execution_time = df['Empty ontology execution time']
             
datastreams = df['Datastream']
inferred_triples = df['Inferred Triples']
thrash_instances = df['Thrash instance count']
reasoner_execution_time = df['Reasoner Execution Time']

dataset_execution_time = df['Entire dataset execution time']

# Increase the font size
plt.rcParams.update({'font.size': 22})

# Create a line plot for Inferred Triples
plt.figure(figsize=(10, 6))
plt.bar(ontology_versions, dataset_execution_time)

plt.xlabel('Version')
plt.ylabel('Execution Time in s')
#plt.title('Datastream execution time for each version')
plt.xticks()
plt.grid(True)
plt.tight_layout()
plt.show()

