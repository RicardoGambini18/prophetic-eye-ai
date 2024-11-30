import json
from flask import jsonify, request
from utils.get_embedding import get_embedding


TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def add_experience_units():
  request_body = request.get_json()
  team_member_name = request_body["team_member"]
  project_name = request_body["project"]
  experience_units = request_body["experience_units"]

  team_members = []
  new_team_members = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    if (team_member["name"] != team_member_name):
      new_team_members.append(team_member)
      continue

    projects = []

    for project in team_member["projects"]:
      if (project["name"] != project_name):
        projects.append(project)
        continue

      experience_units_with_embeddings = []

      for experience_unit in experience_units:
        formatted_experience_unit = f"{experience_unit['tech_stack']}:{
          experience_unit['description']}"
        embedding = get_embedding(formatted_experience_unit)
        experience_unit["embedding"] = embedding
        experience_units_with_embeddings.append(experience_unit)

      project['experience_units'].extend(experience_units_with_embeddings)
      projects.append(project)

    team_member["projects"] = projects
    new_team_members.append(team_member)

  with open(TEAM_MEMBERS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(new_team_members, f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
