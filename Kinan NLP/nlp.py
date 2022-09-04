import os
import pathlib
import pytextrank
import spacy
import re

path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\readme"
save_path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\testresult"

os.chdir(path)
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("topicrank")

def read_text_file(file_path_read, file_path_write):
    with open(file_path_read, 'r', encoding='ascii', errors='ignore') as f1, open(file_path_write, 'w') as f2:
        try:
            text = f1.read()
        except:
            print(file_path_read)
        else:
            new_text = remove_links(text)
            try:
                doc = nlp(new_text)
            except:
                print(file_path_read)
            else:
                for phrase in doc._.phrases:
                    f2.write(phrase.text+'\n')
                    f2.write(str(phrase.rank)+'\n')
        
def remove_links(text):
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path_read = f"{path}\{file}"
        file_path_write = f"{save_path}\{file}"
        read_text_file(file_path_read, file_path_write)