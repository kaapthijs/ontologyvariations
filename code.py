import glob
from rdflib import Graph
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics
import pandas as pd
import time

# Retrieve all ontology files from the "ontologies" folder
ontology_files = glob.glob("ontologies/*.ttl")

# Create a list to store the data
data = []

# Loop through the ontology files
for ontology_file in ontology_files:
    # Load the ontology
    ontology = Graph()
    try:
        ontology.parse(ontology_file, format="ttl")
    except Exception as e:
        print("Error loading the ontology file:", e)
        continue

    # Initialize reasoner
    #reasoner = DeductiveClosure(RDFS_Semantics)
    reasoner = DeductiveClosure(OWLRL_Semantics, rdfs_closure=True, axiomatic_triples=True, datatype_axioms=True)

    # Ontology inferences
    ontologyexpanded = Graph()
    ontologyexpanded += ontology

    # Measure reasoner execution time
    ontology_start_time = time.time()
    empty_ontology_start_time = time.time()

    # Run reasoner
    reasoner.expand(ontologyexpanded)

    # Measure reasoner execution time
    empty_ontology_end_time = time.time()
    empty_ontology_execution_time = empty_ontology_end_time - empty_ontology_start_time

    # Ontology inferences continuation
    ontologyinferencesonly = ontologyexpanded - ontology

    # Define the query for counting axioms and Thrash instances
    count_axioms_query = prepareQuery(
        """
        SELECT (COUNT(*) AS ?count) WHERE {
            ?subclassA rdfs:subClassOf ?class .
        }
        """
    )
    count_thrash_instances_query = prepareQuery(
        """
        PREFIX thijs2: <urn:webprotege:ontology:eb1b07c2-68da-4f99-a0da-8ad9f4ad5a3d#>
        SELECT (COUNT(?instance) AS ?count)
        WHERE {
            ?instance rdf:type thijs2:Thrash .
        }
        """
    )
    show_thrash_instances_query = prepareQuery(
        """
        PREFIX thijs2: <urn:webprotege:ontology:eb1b07c2-68da-4f99-a0da-8ad9f4ad5a3d#>
        SELECT ?instance
        WHERE {
            ?instance rdf:type thijs2:Thrash .
        }
        """
    )


    # thrash and axioms for the 'empty' ontology
    result = list(ontologyinferencesonly.query(count_thrash_instances_query))
    ontology_thrash_count = result[0]['count'].value

    axiom_result  = list(ontologyinferencesonly.query(count_axioms_query))
    ontology_axiom_count = axiom_result[0]['count'].value

    # print data for 'empty' ontology
    print("-----------------------------------------------------------------")
    print("Ontology: ", ontology_file)
    print("Triples in ontology: ", len(ontology))
    print("Triples in ontology with reasoner run: ", len(ontologyexpanded))
    print("Triples that are inferred: ", len(ontologyinferencesonly))
    print("Ontology subclass axioms", ontology_axiom_count)
    print("Ontology Thrash instance count:", ontology_thrash_count)
    print("Empty ontology execution time", empty_ontology_execution_time)

    # Retrieve all datastream files from the "datastreams" folder
    datastream_files = glob.glob("datastreams/*.ttl")

    # Loop through the datastreams
    for datastream_file in datastream_files:
        # Load the datastream
        datastream = Graph()
        try:
            datastream.parse(datastream_file, format="ttl")
        except Exception as e:
            print("Error loading datastream file:", datastream_file)
            print(e)
            continue
        
        # Merge ontology and datastream
        graph = ontology + datastream

        # Measure reasoner execution time
        start_time = time.time()

        # Perform reasoning
        reasoner.expand(graph)

        # Measure reasoner execution time
        end_time = time.time()
        reasoner_execution_time = end_time - start_time

        # Inferred triples
        inferences = graph - ontology

        # Count axioms
        axiom_result  = list(inferences.query(count_axioms_query))
        axiom_count = axiom_result[0]['count'].value
  
        # Count Thrash instances
        result = list(inferences.query(count_thrash_instances_query))
        thrash_count = result[0]['count'].value
        
        show_instances = graph.query(show_thrash_instances_query)

        ontology_file_name = ontology_file.split("\\")[1].split(".")[0]
        datastream_file_name = datastream_file.split("\\")[1].split(".")[0]

        # Append the data to the list
        data.append({'Ontology': ontology_file_name, "Ontology inferences": len(ontologyinferencesonly), "Ontology subclass axioms": ontology_axiom_count, "Ontology Thrash instance count": ontology_thrash_count, "Empty ontology execution time": empty_ontology_execution_time, 'Datastream': datastream_file_name, 'Inferred Triples': len(inferences), 'Subclass Axiom count': axiom_count, 'Thrash instance count': thrash_count, 'Reasoner Execution Time': reasoner_execution_time})

        # Print results
        print("-----------------------------------------------------------------")
        print("Ontology: ", ontology_file)
        print("Datastream:", datastream_file)
        print("Amount of inferred triples: ", len(inferences))
        print("Subclass Axiom count:", axiom_count)
        print("Thrash instance count:", thrash_count)
        for row in show_instances:
            instance_iri = row['instance']
            print(f"Instance: {instance_iri}")
        print('Reasoner Execution Time: ', reasoner_execution_time)
    
    # Measure reasoner execution time
    ontology_end_time = time.time()
    ontology_reasoner_execution_time = ontology_end_time - ontology_start_time
    print("Reasoner execution time:", ontology_reasoner_execution_time)
    data.append({'Ontology': ontology_file_name, 'Entire dataset execution time': ontology_reasoner_execution_time})


# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Specify the Excel file name and save the DataFrame to Excel
excel_file = "ontology_datastream_stats.xlsx"
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)