#use this ontology for ec3epd
import csv
from rdflib import Graph, Namespace, RDF, URIRef, Literal
from rdflib.namespace import RDFS, OWL, XSD
import re
import os
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define namespaces for the ontology
ec3 = Namespace("http://example.org/EC3EPDontology#")
foaf = Namespace("http://xmlns.com/foaf/0.1/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()

# Bind namespaces with prefix names
g.bind("ec3", ec3)
g.bind("foaf", foaf)
g.bind("skos", skos)
g.bind("xsd", xsd)

# Add ontology declaration
ontology_uri = URIRef("http://example.org/ontology")
g.add((ontology_uri, RDF.type, OWL.Ontology))

# General function to create URIs for any namespace
def create_uri(namespace, resource_id):
    """Create a URIRef that uses the provided namespace and resource ID."""
    return namespace[resource_id]

# Function to create OWL classes and add them to the graph
def create_class(namespace, class_name, label, comment=None):
    class_uri = create_uri(namespace, class_name)
    g.add((class_uri, RDF.type, OWL.Class))
    g.add((class_uri, RDFS.label, Literal(label)))
    if comment:
        g.add((class_uri, RDFS.comment, Literal(comment)))
    logging.info(f"Class '{label}' added to the graph.")
    return class_uri

# Function to create OWL data properties
def create_data_property(namespace, prop_name, domain_class, data_type, label, comment=None):
    prop_uri = create_uri(namespace, prop_name)
    g.add((prop_uri, RDF.type, OWL.DatatypeProperty))
    g.add((prop_uri, RDFS.domain, domain_class))
    g.add((prop_uri, RDFS.range, data_type))
    g.add((prop_uri, RDFS.label, Literal(label)))
    if comment:
        g.add((prop_uri, RDFS.comment, Literal(comment)))
    logging.info(f"Data Property '{label}' added to the graph.")
    return prop_uri

# Function to clean decimal values (for Mass per Unit)
def clean_decimal(value):
    cleaned_value = re.sub(r'[^\d.]', '', value)
    if cleaned_value:
        try:
            return Literal(float(cleaned_value), datatype=XSD.decimal)
        except ValueError:
            logging.warning(f"Could not convert '{value}' to a decimal.")
            return Literal(value, datatype=XSD.string)
    else:
        return Literal(value, datatype=XSD.string)

# Define the generic Material class and specific material classes based on keywords
material_class = create_class(ec3, "Material", "Material", "A general material class.")
material_classes = {
    "wood": create_class(ec3, "Wood", "Wood", "Material derived from trees, used in construction and manufacturing."),
    "concrete": create_class(ec3, "Concrete", "Concrete", "A composite material of aggregate and cement."),
    "steel": create_class(ec3, "Steel", "Steel", "An alloy of iron, used in construction and manufacturing."),
    "cement": create_class(ec3, "Cement", "Cement", "A binding material used in construction."),
    "gypsum": create_class(ec3, "Gypsum", "Gypsum", "A soft sulfate mineral used in construction."),
    "brick": create_class(ec3, "Concrete", "Concrete", "A composite material often used with bricks."),
    "glass": create_class(ec3, "Glass", "Glass", "A hard, brittle substance used in construction."),
    "aluminium": create_class(ec3, "Aluminium", "Aluminium", "A lightweight, durable metal used in construction."),
    "bituminous": create_class(ec3, "Bituminous", "Bituminous", "Materials containing or resembling bitumen."),
    "ready mix": create_class(ec3, "Concrete", "Concrete", "Ready-mix concrete, a pre-mixed formulation for construction.")
}

# Data properties for materials
create_data_property(ec3, "hasDeclaredUnit", material_class, XSD.string, "Declared Unit", "The unit in which the material is declared.")
create_data_property(ec3, "hasMassPerUnit", material_class, XSD.decimal, "Mass per Declared Unit", "Mass per declared unit of the material.")
create_data_property(ec3, "createdOn", material_class, XSD.dateTime, "Created On", "Creation date of the material.")
create_data_property(ec3, "updatedOn", material_class, XSD.dateTime, "Updated On", "Update date of the material.")
create_data_property(ec3, "hasParent", material_class, material_class, "has Parent", "Indicates the parent material.")

# Path for CSV and output directory
csv_file_path = os.path.join("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\input\\ececpdJsontoCsv.csv")
output_directory = os.path.join("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task", "output")


# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

output_file = os.path.join(output_directory, "ec3epd22.ttl")

# Read the CSV file and process each row
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Determine class based on keywords in the "Name" column
        name_lower = row["Name"].lower()
        class_uri = material_class  # Default to general material class
        for keyword, class_obj in material_classes.items():
            if keyword in name_lower:
                class_uri = class_obj
                break

        individual_uri = create_uri(ec3, row["ID"])
        g.add((individual_uri, RDF.type, class_uri))

        # Add labels and comments
        g.add((individual_uri, RDFS.label, Literal(row["Name"])))
        if row.get("Description"):
            g.add((individual_uri, RDFS.comment, Literal(row["Description"])))

        # Add data properties
        g.add((individual_uri, create_uri(ec3, "hasDeclaredUnit"), Literal(row["Declared Unit"], datatype=XSD.string)))
        g.add((individual_uri, create_uri(ec3, "hasMassPerUnit"), clean_decimal(row["Mass per Declared Unit"])))
        g.add((individual_uri, create_uri(ec3, "createdOn"), Literal(row["Created On"], datatype=XSD.dateTime)))
        g.add((individual_uri, create_uri(ec3, "updatedOn"), Literal(row["Updated On"], datatype=XSD.dateTime)))

        # Handle parent-child relationships
        if row.get("Parent ID"):
            parent_uri = create_uri(ec3, row["Parent ID"])
            g.add((individual_uri, create_uri(ec3, "hasParent"), parent_uri))

# Serialize the graph to Turtle format
owl_data = g.serialize(format='turtle', encoding='utf-8')

# Save Turtle data to a file
with open(output_file, "wb") as f:
    f.write(owl_data)

logging.info(f"TTL ontology generated and saved as {output_file}")

# Extract individuals and their associated properties
individuals_data = []
for s, p, o in g:
    if (s, RDF.type, material_class) in g:
        # Collect individual URIs and their properties
        individuals_data.append({
            "Individual": s,
            "Predicate": p,
            "Object": o
        })

# Convert the extracted data into a DataFrame
df_individuals = pd.DataFrame(individuals_data)

# Display the table of individuals and instances
print(df_individuals)

# OR save the dataframe to a CSV file for later review
output_csv_file = os.path.join(output_directory, "individuals_instances.csv")
df_individuals.to_csv(output_csv_file, index=False)
print(f"Individuals and instances table saved to {output_csv_file}")



