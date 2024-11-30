from os import getenv
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.generate_team_members import generate_team_members
from controllers.generate_tech_stacks import generate_tech_stacks
from controllers.generate_team_member_experiences import generate_team_member_experiences

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


if __name__ == '__main__':
  app.run(
    debug=True,
    port=getenv("APP_PORT")
  )
