#this is latest final tru ontology
import pandas as pd
from owlready2 import *
from rdflib import Graph, Namespace, Literal, RDF, OWL, RDFS

# Load the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\input\\TRU.csv', sep=';')

# Create an ontology with a base IRI
tru = get_ontology("http://example.org/TRUontology#")

# Define classes and properties
with tru:
    class GenericPhysicalObject(Thing):
        pass

    class Bracket_Bracket(Thing):
        pass

    class Droptube_Droptube(Thing):
        pass

    class Sps_Sps(Thing):
        pass

    class Structure_Structure(Thing):
        pass

    class WireSupport_WireSupport(Thing):
        pass

    # Data properties
    class hasTotalCount(DataProperty, FunctionalProperty):
        range = [int]

    class hasVolume(DataProperty, FunctionalProperty):
        range = [float]

    class hasVolumeCount(DataProperty, FunctionalProperty):
        range = [int]

    class hasArea(DataProperty, FunctionalProperty):
        range = [float]

    class hasAreaCount(DataProperty, FunctionalProperty):
        range = [int]

    class hasLength(DataProperty, FunctionalProperty):
        range = [float]

    class hasLengthCount(DataProperty, FunctionalProperty):
        range = [int]

    class hasLengthUnit(DataProperty, FunctionalProperty):
        range = [str]

    class hasVolumeUnit(DataProperty, FunctionalProperty):
        range = [str]

    class hasAreaUnit(DataProperty, FunctionalProperty):
        range = [str]

    class hasQTY(DataProperty, FunctionalProperty):
        range = [int]

    # Object properties
    class hasMaxUserLabel(ObjectProperty):
        range = [Thing]

    class hasCategory(ObjectProperty):
        range = [Thing]

    class hasECClassId(DataProperty, FunctionalProperty):
        range = [str]

# Iterate through the CSV data and create instances
for index, row in df.iterrows():
    class_name = row['ECClassId'].replace(".", "_")  # Replace '.' with '_' to avoid ontology syntax issues
    cls = getattr(tru, class_name, None)

    if cls is None:
        # If the class doesn't exist, use GenericPhysicalObject
        cls = GenericPhysicalObject
    obj = cls()

    # Assign data properties
    obj.hasTotalCount = int(row['total_count'])
    obj.hasVolume = float(row['volume'])
    obj.hasVolumeCount = int(row['volume_count'])
    obj.hasArea = float(row['area'])
    obj.hasAreaCount = int(row['area_count'])
    obj.hasLength = float(row['length'])
    obj.hasLengthCount = int(row['length_count'])
    obj.hasLengthUnit = row['LengthUnit']
    obj.hasVolumeUnit = row['VolumeUnit']
    obj.hasAreaUnit = row['AreaUnit']
    obj.hasQTY = int(row['QTY'])
    obj.hasECClassId = row['ECClassId']

    # Create and link object properties (Ensure proper linkage and values)
    if not pd.isna(row['MAX(ge.[userlabel])']):
        # Create an individual for the label using the ontology's namespace
        label_instance = GenericPhysicalObject("Label_" + str(index))  # Create an individual with a unique name
        label_instance.label = [row['MAX(ge.[userlabel])']]  # Assign the actual value from the CSV
        obj.hasMaxUserLabel = [label_instance]

    if not pd.isna(row['Category']):
        # Create an individual for the category
        category_instance = GenericPhysicalObject("Category_" + str(index))  # Create an individual with a unique name
        category_instance.label = [row['Category']]  # Assign the actual category value from the CSV
        obj.hasCategory = [category_instance]

# Save the ontology to RDF/XML format
tru.save(file="C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\TRU1.owl", format="rdfxml")

# Load the OWL ontology just saved
g = Graph()
g.parse("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\TRU1.owl", format="xml")

# Bind the 'tru' prefix to the desired IRI
tru_ns = Namespace("http://example.org/TRUontology#")
g.bind("tru", tru_ns)

# Serialize it to Turtle format and save to a file
g.serialize(destination="C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\Tru_ontology.ttl", format="turtle")

print("Ontology with 'tru' prefix has been saved as Turtle format.")

# Generate table for instances, including object and data properties and their values
individuals_data = []

for s, p, o in g:
    # Check for object properties like hasCategory and hasMaxUserLabel
    if p == tru_ns.hasCategory or p == tru_ns.hasMaxUserLabel:
        individuals_data.append({
            "Instance": s,
            "Property": p.split('#')[-1],  # Extract the property name
            "Value": str(o)  # Extract the actual value (for categories, user labels, etc.)
        })
    # Check for data properties like hasLength, hasArea, etc.
    elif isinstance(o, Literal):
        individuals_data.append({
            "Instance": s,
            "Property": p.split('#')[-1],  # Extract the property name
            "Value": str(o)  # Get the actual value
        })

# Convert to a pandas DataFrame for displaying and exporting to CSV
df_individuals = pd.DataFrame(individuals_data)

# Display the table of instances and associated values
print(df_individuals)

# Save the dataframe to a CSV file
df_individuals.to_csv("C:\\Users\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\output\\instances_properties.csv", index=False)

print("Instances and properties table saved to CSV.")
