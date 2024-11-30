import json
from flask import jsonify
from utils.convert_enum_to_list import convert_enum_to_list
from constants.tech_stack import TechStack
from utils.openai_client import openai_client

def get_client_requirements_prompt():
  tech_stack_list = convert_enum_to_list(TechStack)
  tech_stack_formatted = ", ".join(tech_stack_list)
  
  return f"""
  You are in charge on generating a complete requirements text for a random project provided from a fictional client consulting a software development team.
  The requirements must follow these rules:
  * Include a detailed functionality and the exactly techstack used for it (only one per functionalitie).
  * The selected techstack must strictly be inside this provided list: {tech_stack_formatted}.
  * Each techstack can appear multiple times but in different functionalities.
  * The functionalities and techstack must be acoorded to the project
  
  You should return a JSON text contained in a sigle element (one paragraph) cointaining the mutiples requirements
  """
  
def generate_client_requirements():
    chat_completion = openai_client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": get_client_requirements_prompt}]
    )
    
    response = chat_completion.choices[0].message.content
    return jsonify({"requirements": response})