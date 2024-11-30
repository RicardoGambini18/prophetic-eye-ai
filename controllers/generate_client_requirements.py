import json
from flask import jsonify
from utils.convert_enum_to_list import convert_enum_to_list
from constants.tech_stack import TechStack
from utils.openai_client import openai_client


DATASET_SIZE = 10
CLIENT_REQUIREMENTS_DATASET_PATH = "generated/client_requirements.json"


def get_client_requirements_prompt():
  tech_stack_list = convert_enum_to_list(TechStack)
  tech_stack_formatted = ", ".join(tech_stack_list)

  return f"""
    You are tasked to generate structured client requirements for a software project.
    Your response must be a JSON object with the following structure:
    {{
      "name": "The name of the project",
      "requirements": "A clear and concise text that outlines specific functions or features the project requires.
                      Each function or feature should be described in a way that relates it to a specific technology
                      (if applicable) from the provided tech stack list. Requirements should focus on actionable,
                      deliverable tasks or objectives without additional formatting such as subtitles."
    }}

    The provided tech stack list is:
    {tech_stack_formatted}

    Guidelines for generating the requirements:
    - Use the tech stack list to map functions or features to relevant technologies where possible.
    - Write requirements as clear, concise, and professional text, avoiding bullet points, subtitles, or extraneous details.

    Example JSON structure:
    {{
      "name": "Example Client/Project Name",
      "requirements": "The project requires a web application with user authentication implemented using Python.
                      The front-end must be developed using ReactJS, ensuring a responsive and dynamic interface.
                      The application should be containerized and deployed using Docker for scalability."
    }}
  """


def generate_client_requirements():
  client_requirements = []

  for _ in range(DATASET_SIZE):
    chat_completion = openai_client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      messages=[
        {"role": "user", "content": get_client_requirements_prompt()}]
    )

    response = chat_completion.choices[0].message.content
    client_requirement = json.loads(response)
    client_requirements.append(client_requirement)

  with open(CLIENT_REQUIREMENTS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(client_requirements, f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
