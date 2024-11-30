from flask import jsonify, request
from utils.get_experience_units import get_experience_units


def get_team_member_experience_units():
  project_description = request.get_json()["project_description"]
  experience_units = get_experience_units(project_description)
  return jsonify(experience_units)
