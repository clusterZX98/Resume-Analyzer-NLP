
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger")

import re
import string
import nltk
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ----------------------------
# Download Required Resources
# ----------------------------

def download_nltk_resources():
    resources = [
        "punkt",
        "punkt_tab",      # Required for newer NLTK versions
        "stopwords",
        "wordnet",
        "omw-1.4",
        "averaged_perceptron_tagger"
    ]

    for resource in resources:
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(resource)


download_nltk_resources()

# ----------------------------
# Load SpaCy Model
# ----------------------------

try:
    nlp = spacy.load("en_core_web_sm")
except:
    raise Exception(
        "SpaCy model not found.\nRun:\npython -m spacy download en_core_web_sm"
    )

# ----------------------------
# Initialize Objects
# ----------------------------

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

# ----------------------------
# Text Cleaning
# ----------------------------

def clean_text(text: str):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"\S+@\S+", "", text)

    text = re.sub(r"\d+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = re.sub(r"\s+", " ", text).strip()

    return text


# ----------------------------
# Tokenization
# ----------------------------

def tokenize(text):

    return word_tokenize(text)


# ----------------------------
# Remove Stopwords
# ----------------------------

def remove_stopwords(tokens):

    return [

        word

        for word in tokens

        if word not in stop_words

    ]


# ----------------------------
# Lemmatization
# ----------------------------

def lemmatize(tokens):

    return [

        lemmatizer.lemmatize(word)

        for word in tokens

    ]


# ----------------------------
# POS Tagging
# ----------------------------

def pos_tagging(tokens):

    return nltk.pos_tag(tokens)


# ----------------------------
# Named Entity Recognition
# ----------------------------

def named_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append(

            {

                "Text": ent.text,

                "Label": ent.label_

            }

        )

    return entities


# ----------------------------
# Complete NLP Pipeline
# ----------------------------

def process_text(text):

    cleaned = clean_text(text)

    tokens = tokenize(cleaned)

    tokens = remove_stopwords(tokens)

    lemmas = lemmatize(tokens)

    pos = pos_tagging(lemmas)

    ner = named_entities(text)

    return {

        "original_text": text,

        "cleaned_text": cleaned,

        "tokens": tokens,

        "lemmatized_tokens": lemmas,

        "pos_tags": pos,

        "named_entities": ner

    }


# ----------------------------
# Testing
# ----------------------------

if __name__ == "__main__":

    sample = """
    John Doe is a Data Scientist at Google.
    He has 5 years of experience in Python,
    Machine Learning, SQL and TensorFlow.
    """

    result = process_text(sample)

    from pprint import pprint

    print(result)