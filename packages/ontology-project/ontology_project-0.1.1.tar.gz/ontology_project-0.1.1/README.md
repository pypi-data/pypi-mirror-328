# 🏰 Ontology Project

This package **converts CSV files into RDF/OWL ontologies** in TTL format and **merges them** using SBERT-based entity matching.

---

## 📌 Project Structure
Your project is structured as follows:

```
ontology_project/
│-- ontology_project/               # Python package
│   │-- __init__.py                 # Marks as a package
│   │-- Ec3EpdCsv_to_Ec3Epd_onto1.py  # Converts EC3EPD CSV to TTL
│   │-- TruCsv_to_Tru_onto2.py       # Converts TRU CSV to TTL
│   │-- McpCsv_to_Mcp_onto3.py       # Converts MCP CSV to TTL
│   │-- merge_ontology.py            # Merges all TTL files
│   │-- runner.py                    # Automates the pipeline
│
│-- input/                           # CSV input files (Not included in package)
│-- output/                          # Stores generated TTL files (Not included in package)
│-- config.json                      # Stores file paths (Optional)
│-- pyproject.toml                    # Packaging metadata
│-- requirements.txt                  # Dependencies
│-- README.md                         # Documentation
│-- LICENSE                           # License file
│-- .gitignore                        # Ignore unnecessary files
```

---

## 🚀 **Installation**
### 🔹 **Install from PyPI**
After uploading your package to PyPI, install it via:
```sh
pip install ontology_project
```

### 🔹 **Install Locally (Development Mode)**
If you want to modify the package, install it locally:
```sh
pip install -e .
```

---

## ⚡ **Usage**
Once installed, you can **run the following CLI commands**:

| Command | Description |
|---------|-------------|
| `convert_ec3` | Converts EC3EPD CSV to TTL |
| `convert_tru` | Converts TRU CSV to TTL |
| `convert_mcp` | Converts MCP CSV to TTL |
| `merge_ontologies` | Merges all TTL files |
| `run_ontology` | Runs the full pipeline |

Example:
```sh
convert_ec3
convert_tru
convert_mcp
merge_ontologies
run_ontology
```

---

## 🛠 **Building the Package**
### ✅ **Step 1: Install Required Tools**
```sh
pip install build twine
```

### ✅ **Step 2: Build the Package**
```sh
python -m build
```

### ✅ **Step 3: Test Installation**
```sh
pip install dist/ontology_project-0.1.0-py3-none-any.whl
```

### ✅ **Step 4: Upload to PyPI**
```sh
twine upload dist/*
```

---

## 🎯 **Configuration**
You can modify **file paths** in `config.json`:
```json
{
  "input_paths": {
    "ec3epd": "input/ec3epd.csv",
    "tru": "input/tru.csv",
    "mcp": "input/mcp.csv"
  },
  "output_paths": {
    "ec3epd": "output/ec3epd.ttl",
    "tru": "output/tru.ttl",
    "mcp": "output/mcp.ttl",
    "merged": "output/merged_ontology.ttl"
  }
}
```

---

## 🐜 **License**
This project is licensed under the **MIT License**.

---

## 👨‍💻 **Contributing**
We welcome contributions! Please:
- **Fork the repository** on GitHub
- **Create a new branch** (`feature/new-feature`)
- **Submit a pull request**

---

## 🌍 **Resources**
- 📖 **Read the documentation**: [PyPI Project Page](https://pypi.org/project/ontology_project/)
- 🛠 **Report an issue**: [GitHub Issues](https://github.com/yourusername/ontology_project/issues)

---

🚀 **Now try this!** This `README.md` will be **displayed correctly in GitHub, PyPI, and Visual Studio Code.** 😊 Let me know if you need further improvements!

