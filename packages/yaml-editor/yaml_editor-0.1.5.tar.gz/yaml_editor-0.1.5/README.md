# YAML Editor

A web-based YAML editor with a tabular interface that makes it easy to view and edit YAML files.

## Features

- Web-based interface for editing YAML files
- Tabular view of YAML data
- Add and delete rows
- Search functionality
- Real-time editing
- File browser for YAML files

## Installation

Install using pip:

```bash
pip install yaml-editor
```

Or install from source using Poetry:

```bash
git clone https://github.com/yourusername/yaml-editor.git
cd yaml-editor
poetry install
```

## Usage

Start the YAML editor by running:

```bash
yaml-editor
```

Options:
- `--host`: Host to bind the server to (default: 127.0.0.1)
- `--port`: Port to bind the server to (default: 8000)

Example:
```bash
yaml-editor --host 0.0.0.0 --port 8080
```

Once started, open your web browser and navigate to the displayed URL to use the YAML editor.