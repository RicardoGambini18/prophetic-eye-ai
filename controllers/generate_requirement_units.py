import json
from flask import jsonify
from utils.get_requirement_units import get_requirement_units


CLIENT_REQUIREMENTS_DATASET_PATH = "generated/client_requirements.json"


def generate_requirement_units():
  client_requirements = []
  client_requirements_with_units = []

  with open(CLIENT_REQUIREMENTS_DATASET_PATH, 'r') as file:
    client_requirements = json.load(file)

  for client_requirement in client_requirements:
    requirement_units = get_requirement_units(
      client_requirement['requirements'])

    client_requirement['requirement_units'] = requirement_units
    client_requirements_with_units.append(client_requirement)
    print(f"Finished client {client_requirement["name"]}")

  with open(CLIENT_REQUIREMENTS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(client_requirements_with_units,
              f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
