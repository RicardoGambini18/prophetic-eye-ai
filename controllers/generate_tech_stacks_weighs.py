from flask import jsonify, request
from utils.openai_client import openai_client

def get_tech_stack_weights_prompt(project_requirements: str, tech_stack_list: list):
    tech_stack_formatted = ", ".join(tech_stack_list)
    
    return f"""
    You are a software engineer and now you have the responsability to assign weights to each item of a tech stack list based on the project requirements given by a client.
    This is the project requirement: {project_requirements}.
    And these are the items for the tech_stack_list: {tech_stack_formatted}
    
    You have to follow these rules to assign weights:
    * All of the weights must sum 1 (each weight must be from 0 to 1.0).
    * Be the most realistic possible taking in count the different layers on software development and project nature (not the same web development and mobile development).

    You have to return a JSON response with the following structure:
    {{
        tech_stack_weighted = [
            {
                "name": "name",
                "weight": "weight"
            }
        ]
    }}
    """
def generate_tech_stack_weights():
    body = request.data
    tech_stack_list = [item["tech_stack"] for item in body['tech_stack']]
    
    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
          {"role": "user", "content": get_tech_stack_weights_prompt(body['requirements'], tech_stack_list)}]
      )
    
    response = chat_completion.choices[0].message.content
    return jsonify({"tech_stack_weighted": response})