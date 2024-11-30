import json
from flask import jsonify, request
from utils.convert_enum_to_list import convert_enum_to_list
from constants.tech_stack import TechStack
from utils.openai_client import openai_client


TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def get_requirement_units_prompt(project_requirements: str):
  tech_stack_list = convert_enum_to_list(TechStack)
  tech_stack_formatted = ", ".join(tech_stack_list)

  return f"""
  You are tasked with analyzing the following project requirements provided by a client consulting a software development consultancy:
  {project_requirements}
  
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
    body = request.data
    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
          {"role": "user", "content": get_requirement_units_prompt(body['requirements'])}]
      )
    
    response = chat_completion.choices[0].message.content
    return jsonify({"requirement_units": response})
