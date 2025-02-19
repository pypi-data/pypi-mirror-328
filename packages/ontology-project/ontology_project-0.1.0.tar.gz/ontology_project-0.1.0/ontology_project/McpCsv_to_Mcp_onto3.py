
#Final version

import pandas as pd
import rdflib
from rdflib.namespace import RDF, RDFS, XSD, OWL
import urllib.parse

# Path to the input file
input_file_path = 'C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\input\\MCP_carbon.csv'  # Update this path to your actual file path

# Read the data into a DataFrame
df = pd.read_csv(input_file_path)

# Create a new RDF graph
g = rdflib.Graph()

# Define namespaces
mcp = rdflib.Namespace("http://mcpdata.org/")
g.bind("mcp", mcp)

# Define classes
StructuralElement = rdflib.URIRef(mcp.StructuralElement)
Material = rdflib.URIRef(mcp.Material)
Category = rdflib.URIRef(mcp.Category)

# Add classes to the graph
g.add((StructuralElement, RDF.type, OWL.Class))
g.add((Material, RDF.type, OWL.Class))
g.add((Category, RDF.type, OWL.Class))

# Define subclasses
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
asset_code = rdflib.URIRef(mcp.assetCode)
asset_name = rdflib.URIRef(mcp.assetName)
quantity = rdflib.URIRef(mcp.quantity)
unit = rdflib.URIRef(mcp.unit)
total = rdflib.URIRef(mcp.total)
not_specified = rdflib.URIRef(mcp.notSpecified)

# Add data properties to the graph
for prop in [asset_code, asset_name, quantity, unit, total, not_specified]:
    g.add((prop, RDF.type, OWL.DatatypeProperty))
    g.add((prop, RDFS.domain, StructuralElement))

g.add((asset_code, RDFS.range, XSD.string))
g.add((asset_name, RDFS.range, XSD.string))
g.add((quantity, RDFS.range, XSD.float))
g.add((unit, RDFS.range, XSD.string))
g.add((total, RDFS.range, XSD.float))
g.add((not_specified, RDFS.range, XSD.float))

# Iterate over the DataFrame and create RDF triples
for _, row in df.iterrows():
    structural_element = rdflib.URIRef(f"http://example.org/structuralElement/{urllib.parse.quote(str(row['Asset Code']))}")
    category = rdflib.URIRef(f"http://example.org/category/{urllib.parse.quote(str(row['Category']))}")
    
    g.add((structural_element, RDF.type, StructuralElement))
    g.add((structural_element, hasCategory, category))
    g.add((structural_element, asset_code, rdflib.Literal(row['Asset Code'], datatype=XSD.string)))
    g.add((structural_element, asset_name, rdflib.Literal(row['Asset Name'], datatype=XSD.string)))
    g.add((structural_element, quantity, rdflib.Literal(row['Quantity'], datatype=XSD.float)))
    g.add((structural_element, unit, rdflib.Literal(row['Unit'], datatype=XSD.string)))
    g.add((structural_element, total, rdflib.Literal(row['Total'], datatype=XSD.float)))
    #g.add((structural_element, not_specified, rdflib.Literal(row['Not specified'], datatype=XSD.float)))

    # Add material relations
    for material in materials:
        if row[material] != 0:
            material_uri = rdflib.URIRef(mcp[material])
            g.add((structural_element, hasMaterial, material_uri))

# Serialize the graph to a TTL file
output_file = "C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\Mcp_ontology.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Ontology has been saved to {output_file}")
