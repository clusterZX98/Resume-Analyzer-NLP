from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def match_resume_job(resume, job):

   vectorizer = TfidfVectorizer()

   vectors = vectorizer.fit_transform([resume, job])

   similarity = cosine_similarity(vectors)

   score = similarity[0][1]

   return round(score*100,2)