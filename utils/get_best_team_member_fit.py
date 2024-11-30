import json
from utils.openai_client import openai_client


def format_team_members(team_members):
  formatted_string = []

  for index, team_member in enumerate(team_members):
    experience_units = team_member["experience_units"]
    experience_str = []
    for experience_unit in experience_units:
      experience_str.append(
        f"  - Description: {experience_unit['description']}\n"
        f"    Tech Stack: {experience_unit['tech_stack']}\n"
      )

    formatted_string.append(
        f"ID: {index}\n"
        f"Name: {team_member['name']}\n"
        f"English Level: {team_member['english']}\n"
        f"Seniority: {team_member['seniority']}\n"
        f"Tech Stack: {', '.join(team_member['tech_stack'])}\n"
        f"Experience Units:\n{"".join(experience_str)}\n"
    )

  return "\n".join(formatted_string)


def get_best_team_member_fit_prompt(client_requirements: str, team_members: list):
  return f"""
    You are tasked with selecting the best team member for a software development project. Below is the project description and a list of available team members. Your job is to analyze the project requirements and the profiles of each team member to determine the best fit.

    ### Project Description:
    {client_requirements}

    ### Team Members:
    Each team member has a unique ID, along with their profile details.
    {format_team_members(team_members)}

    ### Team Member Profile Structure:
    - ID: A unique identifier for the team member.
    - Name: The name of the team member.
    - Seniority: The seniority level of the team member (Trainee, Junior, Mid-level, Senior).
    - English Level: The English proficiency level of the team member (Basic, Proficient, Advanced).
    - Tech Stacks: The list of technologies the team member is proficient in.
    - Experience Units: A list of specific experiences the team member has, formatted as:
      {{
        "description": "A short sentence describing a project or task completed by the team member.",
        "tech_stack": "The technology used for that task."
      }}

    ### Instructions:
    1. Evaluate the project description and its technical requirements.
    2. Compare the requirements with the profiles of each team member, specifically:
      - The relevance of the team member's tech stacks to the project.
      - The applicability of the experience units to the project requirements.
      - Seniority level, ensuring the team member is capable of meeting the project's complexity.
      - English proficiency level, ensuring the team member can effectively communicate if the project requires it.

    3. Select the best-fitting team member and return their unique ID along with the reason why they are the best choice.

    ### Response Format:
    Return a JSON object with the following structure:
    {{
      "selected_team_member_id": "ID of the selected team member",
      "reason": "A clear explanation of why this team member was selected, considering their tech stacks, experience units, seniority, and English level."
    }}

    ### Example Response:
    If the best-fitting team member has the ID "123":
    {{
      "selected_team_member_id": "123",
      "reason": "The team member was selected because they have extensive experience in ReactJS and Node.js, which are critical for the project. Their seniority as a Mid-level developer and Fluent English ensure they can handle both technical complexity and communication effectively."
    }}

    Analyze carefully and provide a well-justified selection.
  """


def get_best_team_member_fit(client_requirements: str, team_members: list):
  chat_completion = openai_client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      messages=[
        {"role": "user", "content": get_best_team_member_fit_prompt(client_requirements, team_members)}]
    )

  response = chat_completion.choices[0].message.content
  team_member_recommendation = json.loads(response)
  selected_team_member_id = team_member_recommendation["selected_team_member_id"]
  selected_team_member = team_members[int(selected_team_member_id)]
  selected_team_member["reason"] = team_member_recommendation["reason"]
  del selected_team_member["experience_units"]
  del selected_team_member["score"]
  return selected_team_member
