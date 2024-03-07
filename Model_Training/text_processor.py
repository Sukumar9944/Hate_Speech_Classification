import spacy
import re
import pandas as pd

# Spacy Object

def text_processor(text):
    processing = spacy.load('en_core_web_md')

    corpus = []

    # Replacing numbers and Special Characters with whitespace
    text = re.sub('[^a-zA-Z\s]', '', text)

    # Convert the String to lowercase
    text = text.lower()

    # Removing Stop word and Lemmatisation
    doc = processing(text)

    text = ' '.join([word.lemma_ for word in doc if not word.is_stop])
    text = re.sub('\s+', ' ', text)

    text_dict = {'text':text}

    corpus.append(text_dict)

    df = pd.DataFrame(data = corpus)

    return df