import os
import csv

# Remember to change directories
input_directory="./no_punct_POS-tags/UK/"        
output_directory="./most_frequent_words/"

def extract_frequent_words(input_dir, filename, output_dir):
    
    # Import tagged speech
    f = open(os.path.join(input_dir, filename), "r", encoding="utf-8-sig")
    reader = csv.reader(f)
    lista = list(reader)
    
    # Select lemmas of nouns, verbs and adjectives
    l_content=[]
    for row in lista:
        if row[2]=="NOUN" or row[2]=="VERB" or row[2]=="ADJ" or row[2]=="ADV":  # select POS categories
            l_content.append(row[1])  # append lemma
    
    # Count frequency
    freq_count={}
    for word in l_content:
        if word in freq_count:
            freq_count[word] += 1
        else:
            freq_count[word] = 1
    
    freq_count = sorted(freq_count.items(), key= lambda x : x[1], reverse = True)
    
    # Select 3 most frequent words
    lista_tre=[]
    for tupla in freq_count[:5]:    # take four most frequent words
        lista_tre.append(tupla[0])  
    tre_parole = ", ".join(lista_tre)
    
    # Year in the first column - take it from the original filename
    year = filename[-8:-4]
    
    # Write to CSV that already exists!
    new_f = open(os.path.join(output_dir, "UK.csv"), "a", encoding='utf-8-sig', newline="")
    fieldnames = ['YEAR', 'MOST FREQUENT WORDS']
    writer = csv.DictWriter(new_f, fieldnames=fieldnames)
    writer.writerow({'YEAR': year, 'MOST FREQUENT WORDS': tre_parole})
    new_f.close()

# Apply to all files in the input directory
for file in os.listdir(input_directory):
    if file.endswith(".csv"):
        extract_frequent_words(input_directory, file, output_directory)
  