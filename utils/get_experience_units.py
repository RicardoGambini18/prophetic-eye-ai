import json
from utils.convert_enum_to_list import convert_enum_to_list
from constants.tech_stack import TechStack
from utils.openai_client import openai_client


def get_experience_units_prompt(project_description: str):
  tech_stack_list = convert_enum_to_list(TechStack)
  tech_stack_formatted = ", ".join(tech_stack_list)

  return f"""
  You are tasked with analyzing the following project description provided by a software engineer:
  {project_description}

  Extract and return a JSON array where each entry represents a specific experience unit from the project.
  An experience unit consists of:
  1. A concise sentence describing a specific function, feature, or task within the project (`description`).
  2. A single technology explicitly used for that function (`tech_stack`).

  The rules are as follows:
  - Each entry must relate strictly to **one technology** from the provided list:
    {tech_stack_formatted}
  - The same technology can appear in multiple entries if it is used for different functions.
  - Sentences must be short, clear, and focus on one specific function or feature.
  - Ignore any information unrelated to the provided `tech_stack`.

  The JSON format should look like this:
  {{
    "experience_units": [
      {{"description": "Description of a specific function or task",
        "tech_stack": "Technology name"}},
      {{"description": "Description of another function or task",
        "tech_stack": "Technology name"}},
      ...
    ]
  }}

  Only include entries that can clearly relate a project function to a technology from the provided list.
  """


def get_experience_units(project_description: str):
  chat_completion = openai_client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
      {"role": "user", "content": get_experience_units_prompt(project_description)}]
  )

  response = chat_completion.choices[0].message.content
  experience_units = json.loads(response)['experience_units']
  return experience_units
