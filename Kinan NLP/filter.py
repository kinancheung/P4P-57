import os

path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\testresult"
save_path = r"C:\Users\Kinan\Documents\Homework\P4P\readmes\filtered"
word_list = ['wasm', 'web assembly', 'webassembly', 'emscripten']

os.chdir(path)

def read_for_keywords(file_path_read, file_path_write):
    with open(file_path_read, 'r') as f1, open(file_path_write, 'w') as f2:
        try:
            text = f1.read()
        except:
            print(file_path_read)
        else:
            try:
                for item in word_list:
                    if item in text:
                        print('cheese')
            except:
                print(file_path_read)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path_read = f"{path}\{file}"
        file_path_write = f"{save_path}\{file}"
        read_for_keywords(file_path_read, file_path_write)