from utils.calculate_similarity import calculate_similarity


def get_team_member_score(team_member: dict, requirement_units: list, tech_stack_weights: list):
  score = 0

  for project in team_member["projects"]:
    for experience_unit in project['experience_units']:
      for requirement_unit in requirement_units:
        weight = next(
          (item for item in tech_stack_weights if item["name"] == requirement_unit['tech_stack']), {"weight": 0})["weight"]

        similarity = calculate_similarity(
          requirement_unit['embedding'], experience_unit['embedding'])

        score += similarity * weight

  return score
