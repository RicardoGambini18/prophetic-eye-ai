import json
from flask import jsonify

TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def get_projects():
  team_members = []
  projects = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    for project in team_member["projects"]:
      projects.append({
        "name": project["name"]
      })

  return jsonify(projects)
