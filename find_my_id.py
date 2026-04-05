import os
from dotenv import load_dotenv
from frameioclient import FrameioClient

load_dotenv()
client = FrameioClient(os.getenv("FRAMEIO_TOKEN"))

# This will list every project you have access to
projects = client.projects.list_activities_for_account(client.users.get_me()['account_id'])

print("--- YOUR PROJECTS ---")
for p in client.projects.list_projects_for_team(os.getenv("FRAMEIO_TEAM_ID")): # If you have a Team ID
    print(f"NAME: {p['name']} | ID: {p['id']}")