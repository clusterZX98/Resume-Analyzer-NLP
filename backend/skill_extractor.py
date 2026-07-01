
import pandas as pd

skills_db = pd.read_csv("data/skills.csv")

skills = skills_db["Skill"].tolist()

def extract_skills(text):

   extracted = []

   for skill in skills:

       if skill.lower() in text.lower():

           extracted.append(skill)

   return extracted