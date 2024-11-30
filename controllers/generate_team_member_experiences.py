import json
from flask import jsonify
from utils.openai_client import openai_client

TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def get_team_member_experience_prompt(team_member: dict):
  tech_stack_formatted = ", ".join(team_member.get("tech_stack", []))
  english_level = team_member.get("english_level", "Not specified")
  seniority = team_member.get("seniority", "Not specified")

  return f"""
    You are a software developer with the following profile:
    - Tech Stack: {tech_stack_formatted}
    - English Level: {english_level}
    - Seniority: {seniority}

    Write about two invented software projects you have worked on, formatted as a JSON object with the following structure:

    {{
      "projects": [
        {{
          "name": "Name of the project",
          "experience": "A single paragraph describing the project. Include what the project was about, the challenges faced, the solutions implemented, and the overall impact. Use a professional tone and focus on technical and problem-solving skills."
        }}
      ]
    }}

    The project experience must be written in first person and should not contain subtitles.
  """


def generate_team_member_experiences():
  team_members = []
  team_members_with_experience = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
          {"role": "user", "content": get_team_member_experience_prompt(team_member)}]
    )

    response = chat_completion.choices[0].message.content
    projects = json.loads(response)['projects']

    team_member["projects"] = projects
    team_members_with_experience.append(team_member)

    print(f"Finished team member {team_member["name"]}")

  with open(TEAM_MEMBERS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(team_members_with_experience, f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
