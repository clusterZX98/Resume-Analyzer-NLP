def ats_score(resume_skills, job_skills):

   matched = len(
       set(resume_skills)
       &
       set(job_skills)
   )

   score = matched/len(job_skills)

   return round(score*100,2)