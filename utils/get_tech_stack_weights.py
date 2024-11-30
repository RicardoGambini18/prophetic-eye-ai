import json
from utils.openai_client import openai_client


def get_tech_stack_weights_prompt(client_requirements: str, tech_stacks: list):
  tech_stack_formatted = ", ".join(tech_stacks)
  return f"""
    You are a software engineer responsible for assigning weights to each item in a tech stack list based on the client's project requirements.

    ### Project Requirements:
    {client_requirements}

    ### Tech Stack List:
    {tech_stack_formatted}

    ### Instructions:
    - Assign a weight to each technology based on its importance to the project requirements.
    - All weights must sum to **1**. Each weight should be a value between **0** and **1**, inclusive.
    - Base your weights on realistic considerations of the project's nature, such as:
      - The layers of software development involved (e.g., front-end, back-end, database, infrastructure).
      - The type of project (e.g., web development, mobile development, data analysis).
    - Only assign non-zero weights to technologies that are explicitly or implicitly relevant to the requirements.
    - Technologies not needed for the project should have a weight of **0**.

    ### Response Format:
    Return a JSON object structured as follows:
    {{
      "tech_stack_weights": [
          {{
              "name": "Technology name",
              "weight": "Weight value"
          }},
          ...
      ]
    }}

    ### Example Response:
    If the project is a web application and the tech stack includes Python, ReactJS, and Docker, an example output might look like this:
    {{
      "tech_stack_weights": [
          {{
              "name": "Python",
              "weight": 0.5
          }},
          {{
              "name": "ReactJS",
              "weight": 0.4
          }},
          {{
              "name": "Docker",
              "weight": 0.1
          }}
      ]
    }}

    Ensure the weights are logical and align with the provided requirements.
  """


def get_tech_stack_weights(client_requirements: str, tech_stacks: list):
  chat_completion = openai_client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      messages=[
        {"role": "user", "content": get_tech_stack_weights_prompt(client_requirements, tech_stacks)}]
    )

  response = chat_completion.choices[0].message.content
  tech_stack_weights = json.loads(response)['tech_stack_weights']
  return tech_stack_weights
