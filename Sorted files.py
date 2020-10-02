import os

def get_path(*args):
    file_path = os.path.join(os.getcwd(), *args)
    return file_path

files_list = [get_path('sorted', file) for file in os.listdir(get_path('sorted'))]
len_files_list = list()
for file_ in files_list:
    with open(file_, encoding='utf-8') as file_text:
        lines = file_text.readlines()
        len_files_list.append(len(lines))
sorted_list = sorted(list(zip(files_list, len_files_list)), key=lambda x: x[1])
with open('sorted.txt', 'w', encoding='utf=8') as sorted_text:
    for file_ in sorted_list:
        with open(file_[0], encoding='utf-8') as file_text:
            lines = file_text.readlines()
            sorted_text.write(os.path.basename(file_[0]) + '\n')
            sorted_text.write(str(len(lines)) + '\n')
            for line in lines:
                sorted_text.write(line)
            sorted_text.write('\n\n')

with open('sorted.txt', encoding='utf-8') as text:
    print(text.read())