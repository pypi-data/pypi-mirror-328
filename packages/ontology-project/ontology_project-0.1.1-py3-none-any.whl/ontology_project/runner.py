import subprocess
import json
import os

# Load configuration
with open("C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\config.json", "r") as f:
    config = json.load(f)

# Ensure output directory exists
for path in config["output_paths"].values():
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Run existing scripts with correct paths
subprocess.run(["python", "C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\ontology_project\\Ec3EpdCsv_to_Ec3Epd_onto1.py"])
subprocess.run(["python", "C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\ontology_project\\TruCsv_to_Tru_onto2.py"])
subprocess.run(["python", "C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\ontology_project\\McpCsv_to_Mcp_onto3.py"])

print("All ontology files have been generated successfully!")

# Run merging script
subprocess.run(["python", "C:\\Users\\pb21\\OneDrive - National Physical Laboratory\\Documents\\OneNote Notebooks\\W6_Task\\ontology_project\\merge_ontology.py"])

print("Ontology generation and merging complete!")