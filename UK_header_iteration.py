# If stanza is not installed, run the following command
#pip install stanza

# Otherwise access the stanza venv (virtual environment)
"""
$ source stanza2/bin/activate
"""

import stanza

# If you haven't downloaded the right language package, uncomment the following line
stanza.download('en')

# Remember to change language!!
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma')

import os
import csv

# Input and output directories
txt_directory="./corpus/UK/"
csv_directory="./no_punct_POS-tags/UK/"

def apply_stanza (input_dir, filename, output_dir):
    txt_file = open(os.path.join(input_dir, filename), "r", encoding="utf-8").read()
    doc = nlp(txt_file.lower())
    speech_pos = [[word.text, word.lemma, word.upos, word.feats if word.feats else "_"] for sent in doc.sentences for word in sent.words]

    # Remove elementS that are tagged 'PUNCT'
    no_punctuation = []
    for x in speech_pos:
        if x[2] == "PUNCT":
            pass
        else:
            no_punctuation.append(x)
    
    rows = zip(no_punctuation)    # access each item in the list

    csv_filename= filename.replace(".txt", ".csv")
    
    headers= ["TOKEN", "LEMMA", "POS-TAG", "MORPHOLOGICAL FEATURES"]

# Output .csv file with POS-tags
    f = open(os.path.join(output_dir, csv_filename), "w")  # path.join gives the correct path to the .csv file
    writer = csv.writer(f, delimiter=",", lineterminator="\r\n")
    writer.writerow(headers)
    for row in rows:
        for el in row:
            writer.writerow(el)   # write each word on a different row
    f.close()

for file in os.listdir(txt_directory):
    if file.endswith(".txt"):
        apply_stanza(txt_directory, file, csv_directory)
  