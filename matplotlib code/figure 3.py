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

# Group the data by ontology version
grouped_data = df.groupby('Ontology')
                          
# Define line styles and colors

line_styles = [':']
colors = ['red', 'blue', 'green', 'orange', 'olive', 'purple']

for i, (ontology_version, group) in enumerate(grouped_data):
    thrash_instances = group['Thrash instance count']
    datastreams = group['Datastream'].astype(str)
    plt.plot(datastreams, thrash_instances, marker='o', linestyle=line_styles[i % len(line_styles)], color=colors[i % len(colors)], label=ontology_version)

plt.xlabel('Datastream')
plt.ylabel('Thrash Instances')
plt.title('Thrash Instances vs. Datastream')
plt.legend()
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Remove x-axis tick labels
plt.show()
