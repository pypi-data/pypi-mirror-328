#Use this ontology script fpr MCP. This is latest final

import pandas as pd
import rdflib
from rdflib.namespace import RDF, RDFS, XSD, OWL
import urllib.parse
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Path to the input file
input_file_path = 'C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\input\\MCP_carbon.csv'

# Path to output directory
output_directory = 'C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output'
output_file = os.path.join(output_directory, "MCP_ontology.ttl")

# Read the data into a DataFrame
df = pd.read_csv(input_file_path)

# Create a new RDF graph
g = rdflib.Graph()

# Define namespaces and bind them for proper prefixes
mcp = rdflib.Namespace("http://example.org/MCPCarbonontology#")
#mcp = rdflib.Namespace("http://mcpdata.org/")
foaf = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
xsd = rdflib.Namespace("http://www.w3.org/2001/XMLSchema#")

g.bind("mcp", mcp)
g.bind("foaf", foaf)
g.bind("skos", skos)
g.bind("xsd", xsd)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("owl", OWL)

# Define and add classes
StructuralElement = rdflib.URIRef(mcp.StructuralElement)
Material = rdflib.URIRef(mcp.Material)
Category = rdflib.URIRef(mcp.Category)
g.add((StructuralElement, RDF.type, OWL.Class))
g.add((Material, RDF.type, OWL.Class))
g.add((Category, RDF.type, OWL.Class))

# Define subclasses of Material
materials = ["Concrete", "Steel", "Glass", "Wood", "Clay", "Plastic", "Aluminium", "Iron", "Copper", "Bitumen", "Cement"]
for material in materials:
    material_uri = rdflib.URIRef(mcp[material])
    g.add((material_uri, RDF.type, OWL.Class))
    g.add((material_uri, RDFS.subClassOf, Material))

# Define object properties
hasMaterial = rdflib.URIRef(mcp.hasMaterial)
hasCategory = rdflib.URIRef(mcp.hasCategory)
g.add((hasMaterial, RDF.type, OWL.ObjectProperty))
g.add((hasMaterial, RDFS.domain, StructuralElement))
g.add((hasMaterial, RDFS.range, Material))

g.add((hasCategory, RDF.type, OWL.ObjectProperty))
g.add((hasCategory, RDFS.domain, StructuralElement))
g.add((hasCategory, RDFS.range, Category))

# Define data properties
properties = {
    "Asset Code": (mcp.assetCode, XSD.string),
    "Asset Name": (mcp.assetName, XSD.string),
    "Quantity": (mcp.quantity, XSD.float),
    "Unit": (mcp.unit, XSD.string),
    "Total": (mcp.total, XSD.float),
    "Not specified": (mcp.notSpecified, XSD.float)
}

# Add data properties to the graph
for prop, (prop_uri, data_type) in properties.items():
    g.add((prop_uri, RDF.type, OWL.DatatypeProperty))
    g.add((prop_uri, RDFS.domain, StructuralElement))
    g.add((prop_uri, RDFS.range, data_type))

# Iterate over the DataFrame and create RDF triples
for _, row in df.iterrows():
    # Skip rows with missing Asset Code or Asset Name
    if pd.isna(row["Asset Code"]) or pd.isna(row["Asset Name"]):
        continue

    structural_element = rdflib.URIRef(f"http://mcp.org/structuralElement/{urllib.parse.quote(str(row['Asset Code']))}")
    category = rdflib.URIRef(f"http://mcp.org/category/{urllib.parse.quote(str(row['Category']))}")
    
    # Add structural element as an instance of StructuralElement
    g.add((structural_element, RDF.type, StructuralElement))
    g.add((structural_element, hasCategory, category))
    
    # Add data properties if available
    for prop, (prop_uri, data_type) in properties.items():
        if pd.notna(row[prop]):  # Check if value is not NaN
            g.add((structural_element, prop_uri, rdflib.Literal(row[prop], datatype=data_type)))

    # Add material relations if material columns have non-zero values
    for material in materials:
        if pd.notna(row[material]) and row[material] != 0:
            material_uri = rdflib.URIRef(mcp[material])
            g.add((structural_element, hasMaterial, material_uri))

# Serialize the graph to Turtle format and save to a file
owl_data = g.serialize(format='turtle', encoding='utf-8')

# Save Turtle data to a file
with open(output_file, "wb") as f:
    f.write(owl_data)

logging.info(f"TTL ontology generated and saved as {output_file}")

# Extract individuals and their associated properties
individuals_data = []
for s, p, o in g:
    if (s, RDF.type, StructuralElement) in g or (s, RDF.type, Material) in g:
        # Collect individual URIs and their properties
        individuals_data.append({
            "Individual": s,
            "Predicate": p,
            "Object": o
        })

# Convert the extracted data into a DataFrame
df_individuals = pd.DataFrame(individuals_data)

# Display the table of individuals and instances in the console
print(df_individuals)

# OR save the dataframe to a CSV file for later review
output_csv_file = os.path.join(output_directory, "MCP_individuals_instances.csv")
df_individuals.to_csv(output_csv_file, index=False)
print(f"Individuals and instances table saved to {output_csv_file}")
