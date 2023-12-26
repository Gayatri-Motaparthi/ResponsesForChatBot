import json

import spacy
nlp = spacy.load("en_core_web_md")
# nlp = spacy.load("en_core_web_lg")

def getMatch(prompt):
    
    file = open("application/sentences.json")

    data = json.load(file)

    output = []
    output_value = 0
    for key, value in data.items():
        similarity = nlp(prompt).similarity(nlp(key))

        if similarity>output_value:
            output_value = similarity
            output = value

    return output


