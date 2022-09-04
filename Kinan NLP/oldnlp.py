import os
import pathlib
import pytextrank
import spacy
import re

path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\test"
save_path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\testresult"

os.chdir(path)
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("topicrank")

def read_text_file(file_path_read, file_path_write):
    with open(file_path_read, 'r', encoding='ascii', errors='ignore') as f1, open(file_path_write, 'w') as f2:
        try:
            # text = pathlib.Path(f"{file_path_read}").read_text()
            text = f1.read()
        except:
            print(file_path_read)
        else:
            # emoji_removed_text = remove_emojis(text)
            # only_ascii_characters = emoji_removed_text.encode("ascii", "ignore")
            # decoded = only_ascii_characters.decode()
            doc = nlp(text)
            for phrase in doc._.phrases:
                f2.write(phrase.text+'\n')
                f2.write(str(phrase.rank)+'\n')

def remove_emojis(text):
    emojis = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emojis, '', text)
        

for file in os.listdir():
    if file.endswith(".txt"):
        file_path_read = f"{path}\{file}"
        file_path_write = f"{save_path}\{file}"
        read_text_file(file_path_read, file_path_write)
