import typer
from typing import Optional
from typing_extensions import Annotated
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.table import Table
from pydantic import ValidationError

from methodos.models.config import Config

import yaml
import os
import requests

# app = typer.Typer()

def load_config(config_file: Path) -> dict:
  with open(config_file, "r") as f:
    try:
      data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
      print(f"Error loading configuration file: {exc}")
      exit(1)
  return data

def main():
  print(Panel.fit("Lightweight configuration management", title="Methodos"))
  print()

   # Step 1: Define configuration file locations for methodos client configuration.
  config_locations= [
    Path.cwd() / ".methodos" / "config.yaml",
    Path.home() / ".methodos" / "config.yaml",
    Path("/etc/methodos/config.yaml"),
  ]

  # Step 2: Load the first configuration file that exists in the config_locations search order
  config_file = next((location for location in config_locations if location.exists()), None)
  
  if config_file is None:
    print("No configuration file found.")
    print()
    print("Please create a configuration file at one of the following locations:")
    for location in config_locations:
      print(location)
    exit(1)

  print(f"Using configuration file: {config_file}")
  print()

  # Step 3: Load the configuration file
  config_data = load_config(config_file)
  config_data['access_key'] = os.environ.get('METHODOS_ACCESS_KEY', config_data['access_key'])
  config_data['secret_key'] = os.environ.get('METHODOS_SECRET_KEY', config_data['secret_key'])  

  # Step 4: Check configuration against model
  try:
    config = Config(**config_data)
  except ValidationError as e:
    print(f"Configuration is invalid: {e}")
    exit(1)

  # Step 5: Make a request to the nodes server
  check_in = config.node_url + "api/v1/check_in"

  headers = {
    'X-ACCESS-KEY': config.access_key,
    'X-SECRET-KEY': config.secret_key,
    'Content-Type': 'application/json'
  }

  
  



  



      




if __name__ == "__main__":
    main()

