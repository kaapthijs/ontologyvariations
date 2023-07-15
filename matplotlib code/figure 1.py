import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('my_stats.xlsx')

# Extract the required columns
ontology_versions = df['Ontology']
ontology_inferences = df['Ontology inferences']
ontology_subclasses = df['Ontology subclass axioms']
ontology_thrash_instances = df['Ontology Thrash instance count']
ontology_execution_time = df['Empty ontology execution time']
             
datastreams = df['Datastream']
inferred_triples = df['Inferred Triples']
thrash_instances = df['Thrash instance count']
reasoner_execution_time = df['Reasoner Execution Time']

dataset_execution_time = df['Entire dataset execution time']

# Create a line plot for Inferred Triples
plt.figure(figsize=(10, 6))
plt.bar(ontology_versions, dataset_execution_time)
plt.bar(ontology_versions, dataset_execution_time)

plt.xlabel('Version')
plt.ylabel('Entire dataset execution time')
plt.title('Entire dataset execution time vs. Version')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

