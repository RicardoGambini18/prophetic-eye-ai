import json
from faker import Faker
from flask import jsonify
from constants.programming_language_to_tech_stacks import PROGRAMMING_LANGUAGE_TO_TECH_STACKS

fake = Faker()

TECH_STACKS_DATASET_PATH = "generated/tech-stacks.json"


def generate_tech_stacks():
  programming_languages = []

  for programming_language in PROGRAMMING_LANGUAGE_TO_TECH_STACKS.keys():
    programming_languages.append({
      "name": programming_language,
      "tech_stacks": PROGRAMMING_LANGUAGE_TO_TECH_STACKS[programming_language]
    })

  with open(TECH_STACKS_DATASET_PATH, 'w', encoding='utf-8') as f:
    json.dump(programming_languages, f, ensure_ascii=False, indent=2)

  return jsonify({"success": True})
