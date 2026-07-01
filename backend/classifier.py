import joblib

model = joblib.load("models/classifier.pkl")

tfidf = joblib.load("models/tfidf.pkl")

def predict_category(text):

   vector = tfidf.transform([text])

   pred = model.predict(vector)

   return pred[0]