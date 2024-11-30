import json
from flask import jsonify
from utils.get_experience_units import get_experience_units


TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def generate_experience_units():
  team_members = []
  team_members_with_experience_units = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    projects = []
    for project in team_member["projects"]:
      experience_units = get_experience_units(project['experience'])
      project["experience_units"] = experience_units
      projects.append(project)

    team_member["projects"] = projects
    team_members_with_experience_units.append(team_member)
    print(f"Finished team member {team_member["name"]}")

  with open(TEAM_MEMBERS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(team_members_with_experience_units,
              f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
