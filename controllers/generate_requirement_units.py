import json
from flask import jsonify
from utils.convert_enum_to_list import convert_enum_to_list
from constants.tech_stack import TechStack
from utils.openai_client import openai_client


CLIENT_REQUIREMENTS_DATASET_PATH = "generated/client_requirements.json"


def get_requirement_units_prompt(client_requirements: str):
  tech_stack_list = convert_enum_to_list(TechStack)
  tech_stack_formatted = ", ".join(tech_stack_list)

  return f"""
    You are tasked with analyzing the following project requirements provided by a client consulting a software development consultancy:
    {client_requirements}

    Extract and return a JSON array where each entry represents a specific requirement unit from the project.
    An requirement unit consists of:
    1. A concise sentence describing a specific requirement, function, or task within the project (`description`).
    2. A single technology explicitly used for that requirement (`tech_stack`).
    The rules are as follows:
    - Each entry must relate strictly to **one technology** from the provided list:
      {tech_stack_formatted}
    - The same technology can appear in multiple entries if they is used for different requirements.
    - Sentences must be short, clear, and focus on one specific function or feature.
    - Ignore any information unrelated to the provided `tech_stack`.
    The JSON format should look like this:
    {{
      "requirement_units": [
        {{"description": "Description of a specific requirement",
          "tech_stack": "Technology name"}},
        {{"description": "Description of another requirement",
          "tech_stack": "Technology name"}},
        ...
      ]
    }}
    Only include entries that can clearly relate a project function to a technology from the provided list.
  """


def generate_requirement_units():
  client_requirements = []
  client_requirements_with_units = []

  with open(CLIENT_REQUIREMENTS_DATASET_PATH, 'r') as file:
    client_requirements = json.load(file)

  for client_requirement in client_requirements:
    chat_completion = openai_client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      messages=[
        {"role": "user", "content": get_requirement_units_prompt(client_requirement['requirements'])}]
    )

    response = chat_completion.choices[0].message.content
    requirement_units = json.loads(response)['requirement_units']

    client_requirement['requirement_units'] = requirement_units
    client_requirements_with_units.append(client_requirement)
    print(f"Finished client {client_requirement["name"]}")

  with open(CLIENT_REQUIREMENTS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(client_requirements_with_units,
              f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
