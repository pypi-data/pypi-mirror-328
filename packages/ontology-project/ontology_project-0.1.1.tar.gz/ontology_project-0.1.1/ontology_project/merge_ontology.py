from rdflib.namespace import RDF, RDFS, OWL, Namespace
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import rdflib

# Load the Sentence-BERT model
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Define namespaces
ec3_ns = rdflib.Namespace("http://example.org/EC3EPDontology#")
tru_ns = rdflib.Namespace("http://example.org/TRUontology#")
mcp_ns = rdflib.Namespace("http://example.org/MCPCarbonontology#")
ns3 = rdflib.Namespace("http://mcp.org/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

# Function to bind namespaces
def bind_namespaces(graph):
    graph.bind("ec3", ec3_ns)
    graph.bind("tru", tru_ns)
    graph.bind("mcp", mcp_ns)
    graph.bind("ns3", ns3)
    graph.bind("skos", SKOS)

# Load ontologies
def load_ontology(file_path):
    g = rdflib.Graph()
    g.parse(file_path, format="turtle")
    return g

ont1 = load_ontology("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\ec3epd22.ttl") #1_3 matching(9), 1_2 not matching(0)
ont2 = load_ontology("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\Tru_ontology.ttl")#2_3 mactching(40)
ont3 = load_ontology("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\Mcp_ontology.ttl")#1-3, 2-3

# Function to convert text to embeddings using SBERT
def get_embedding(text):
    return sbert_model.encode(text) if text else None

# Function to get textual annotations for an entity in any ontology
def get_textual_info(graph, entity, label_props):
    texts = []
    for prop in label_props:
        texts.extend([str(o) for o in graph.objects(entity, prop)])
    return ' '.join(texts)

# Function to match entities or classes between two ontologies
def match_entities(entities1, entities2, graph1, graph2, label_props1, label_props2, thresholds):
    matches = []
    unmatched_entities1 = set()
    unmatched_entities2 = set()

    for entity1 in entities1:
        text1 = get_textual_info(graph1, entity1, label_props1)
        embedding1 = get_embedding(text1)
        if embedding1 is None:
            continue
        for entity2 in entities2:
            text2 = get_textual_info(graph2, entity2, label_props2)
            embedding2 = get_embedding(text2)
            if embedding2 is None:
                continue
            text_similarity = cosine_similarity([embedding1], [embedding2])[0][0]
            if text_similarity >= thresholds['close']:
                if text_similarity >= thresholds['exact']:
                    match_type = SKOS.exactMatch
                elif text_similarity >= thresholds['narrow']:
                    match_type = SKOS.narrowMatch
                else:
                    match_type = SKOS.closeMatch
                matches.append((entity1, entity2, match_type))
                break
        else:
            unmatched_entities1.add(entity1)
    unmatched_entities2 = entities2 - {match[1] for match in matches}
    return matches, unmatched_entities1, unmatched_entities2

# Add all triples of an entity to the merged graph
def add_entity_data(graph, source_graph, entity):
    for p, o in source_graph.predicate_objects(entity):
        graph.add((entity, p, o))

# Match entities between Ontology 1 and Ontology 3
entities1 = {s for s in ont1.all_nodes() if not isinstance(s, rdflib.BNode)}
entities3 = {s for s in ont3.all_nodes() if not isinstance(s, rdflib.BNode)}

label_props1 = [RDFS.label, RDFS.comment]
label_props3 = [
    rdflib.URIRef("http://example.org/MCPCarbonontology#assetName"),
    rdflib.URIRef("http://example.org/MCPCarbonontology#hasCategory"),
    RDFS.label,
]

thresholds = {
    'exact': 0.8,
    'narrow': 0.7,
    'close': 0.6
}

matches1_3, unmatched1_3, unmatched3_1 = match_entities(
    entities1, entities3, ont1, ont3, label_props1, label_props3, thresholds
)

# Match entities between Ontology 2 and Ontology 3
entities2 = {s for s in ont2.all_nodes() if not isinstance(s, rdflib.BNode)}

label_props2 = [
    rdflib.URIRef("http://example.org/TRUontology#hasECClassId"),
    rdflib.URIRef("http://example.org/TRUontology#hasMaxUserLabel"),
    RDFS.label,
]

matches2_3, unmatched2_3, unmatched3_2 = match_entities(
    entities2, entities3, ont2, ont3, label_props2, label_props3, thresholds
)

# Create merged ontology
merged_graph = rdflib.Graph()
bind_namespaces(merged_graph)

# Add matched entities and their associated data using SKOS properties
def add_matched_entities(graph, matches, graph1, graph2):
    for entity1, entity2, match_type in matches:
        add_entity_data(graph, graph1, entity1)
        add_entity_data(graph, graph2, entity2)
        graph.add((entity1, match_type, entity2))

add_matched_entities(merged_graph, matches1_3, ont1, ont3)
add_matched_entities(merged_graph, matches2_3, ont2, ont3)

# Add unmatched entities
def add_unmatched_entities(graph, unmatched_entities, source_graph):
    for entity in unmatched_entities:
        add_entity_data(graph, source_graph, entity)

add_unmatched_entities(merged_graph, unmatched1_3, ont1)
add_unmatched_entities(merged_graph, unmatched2_3, ont2)
add_unmatched_entities(merged_graph, unmatched3_1 | unmatched3_2, ont3)

# Save the merged ontology
merged_graph.serialize(destination="C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\output\\merged_ontology_with_skos.ttl", format="turtle")
print("Merged ontology saved to 'merged_ontology_with_skos.ttl'.")
