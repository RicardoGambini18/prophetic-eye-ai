import json
import random
from faker import Faker
from flask import jsonify
from utils.convert_enum_to_list import convert_enum_to_list
from utils.get_random_items import get_random_items
from constants.english_level import EnglishLevel
from constants.seniority import Seniority
from constants.tech_stack import TechStack
from constants.programming_language import ProgrammingLanguage
from constants.programming_language_to_tech_stacks import PROGRAMMING_LANGUAGE_TO_TECH_STACKS

fake = Faker()

DATASET_SIZE = 30
TEAM_MEMBERS_DATASET_PATH = "generated/team-members.json"


def generate_team_members():
  team_members = []

  for _ in range(DATASET_SIZE):
    name = fake.name()

    english_level_list = convert_enum_to_list(EnglishLevel)
    english_level = get_random_items(english_level_list)

    seniority_list = convert_enum_to_list(Seniority)
    seniority = get_random_items(seniority_list)

    programming_language_list = convert_enum_to_list(ProgrammingLanguage)
    programming_languages = get_random_items(
      programming_language_list, random.randint(2, 3))

    tech_stack = []

    for programming_language in programming_languages:
      full_tech_stack_list = PROGRAMMING_LANGUAGE_TO_TECH_STACKS.get(
        programming_language)

      if (type(full_tech_stack_list) is list):
        tech_stack_list = get_random_items(
          full_tech_stack_list,
          random.randint(2, 3)
        )
        tech_stack.extend(tech_stack_list)

    team_member = {
      "name": name,
      "english": english_level,
      "seniority": seniority,
      "tech_stack": tech_stack
    }

    team_members.append(team_member)

  with open(TEAM_MEMBERS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(team_members, f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
