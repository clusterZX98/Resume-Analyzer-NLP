import re

education_keywords = [
   "btech",
   "mtech",
   "bca",
   "mca",
   "bsc",
   "msc",
   "b.com",
   "bba",
   "ba"


]

def extract_education(text):

   found = []

   for edu in education_keywords:

       if edu in text.lower():

           found.append(edu.upper())

   return found