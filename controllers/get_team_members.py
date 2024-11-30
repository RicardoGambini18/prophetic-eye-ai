import json
from flask import jsonify

TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def get_team_members():
  team_members = []
  formatted_team_members = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    formatted_team_members.append({
      "name": team_member["name"],
      "english": team_member["english"],
      "seniority": team_member["seniority"],
      "tech_stack": team_member["tech_stack"],
    })

  return jsonify(formatted_team_members)
