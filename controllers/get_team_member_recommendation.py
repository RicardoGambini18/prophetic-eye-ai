import json
import heapq
from flask import jsonify, request
from utils.get_requirement_units import get_requirement_units
from utils.get_tech_stack_weights import get_tech_stack_weights
from utils.get_requirement_units_embeddings import get_requirement_units_embeddings
from utils.get_team_member_score import get_team_member_score
from utils.get_best_team_member_fit import get_best_team_member_fit

TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def get_team_member_recommendation():
  client_requirements = request.get_json()["client_requirements"]
  requirement_units = get_requirement_units(client_requirements)

  tech_stacks = []

  for requirement_unit in requirement_units:
    if requirement_unit['tech_stack'] not in tech_stacks:
      tech_stacks.append(requirement_unit['tech_stack'])

  tech_stack_weights = get_tech_stack_weights(client_requirements, tech_stacks)

  requirement_units_with_embeddings = get_requirement_units_embeddings(
    requirement_units)

  team_members = []
  team_members_with_score = []

  with open(TEAM_MEMBERS_DATASET_PATH, 'r') as file:
    team_members = json.load(file)

  for team_member in team_members:
    score = get_team_member_score(
      team_member, requirement_units_with_embeddings, tech_stack_weights)

    formatted_experience_units = []

    for project in team_member["projects"]:
      for experience_unit in project["experience_units"]:
        formatted_experience_units.append({
          "description": experience_unit['description'],
          "tech_stack": experience_unit['tech_stack']
        })

    team_members_with_score.append({
      "name": team_member["name"],
      "english": team_member["english"],
      "seniority": team_member["seniority"],
      "tech_stack": team_member["tech_stack"],
      "score": score,
      "experience_units": formatted_experience_units
    })

  sorted_team_members = heapq.nlargest(
    8, team_members_with_score, key=lambda x: x['score'])

  team_member_recommendation = get_best_team_member_fit(
    client_requirements, sorted_team_members)

  return jsonify(team_member_recommendation)
