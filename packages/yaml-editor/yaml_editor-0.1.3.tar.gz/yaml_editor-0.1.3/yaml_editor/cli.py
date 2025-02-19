#!/usr/bin/env python3

import click
from .app import main as run_app

@click.command()
@click.option('--host', default='127.0.0.1', help='Host to bind the server to')
@click.option('--port', default=8000, help='Port to bind the server to')
@click.option('--dir', default='.', help='Directory containing YAML files')
def main(host: str, port: int, dir: str):
    """Launch the YAML Editor web interface."""
    run_app(host=host, port=port, yaml_dir_path=dir)

if __name__ == '__main__':
    main()