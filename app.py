from os import getenv
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.generate_team_members import generate_team_members
from controllers.generate_tech_stacks import generate_tech_stacks
from controllers.generate_team_member_experiences import generate_team_member_experiences
from controllers.generate_experience_units import generate_experience_units
from controllers.generate_client_requirements import generate_client_requirements

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
  return "<p>Prophetic Eye API</p>"


@app.post("/api/generate-team-members")
def generate_team_members_controller():
  return generate_team_members()


@app.post("/api/generate-tech-stacks")
def generate_tech_stacks_controller():
  return generate_tech_stacks()


@app.post("/api/generate-team-member-experiences")
def generate_team_member_experiences_controller():
  return generate_team_member_experiences()


@app.post("/api/generate-experience-units")
def generate_experience_units_controller():
  return generate_experience_units()


@app.post("/api/generate-clients-requirements")
def generate_client_requirements_controller():
  return generate_client_requirements()

if __name__ == '__main__':
  app.run(
    debug=True,
    port=getenv("APP_PORT")
  )
