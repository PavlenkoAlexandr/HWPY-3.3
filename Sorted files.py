import os

def get_path(*args):
    file_path = os.path.join(os.getcwd(), *args)
    return file_path

files_list = os.listdir(get_path('sorted'))
sorted_list = sorted([get_path('sorted', file) for file in files_list], key=os.path.getsize)
with open('sorted.txt', 'w', encoding='utf=8') as sorted_text:
    for file_ in sorted_list:
        with open(file_, encoding='utf-8') as file_text:
            lines = file_text.readlines()
            sorted_text.write(os.path.basename(file_) + '\n')
            sorted_text.write(str(len(lines)) + '\n')
            for line in lines:
                sorted_text.write(line)
            sorted_text.write('\n\n')

with open('sorted.txt', encoding='utf-8') as text:
    print(text.read())