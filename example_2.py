# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Строка1\n', 'Строка2\n', 'Строка3\n']

with open("my_file.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("my_file.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f'Символов в линию:{letters}')
    print(f'Количество строк:{lines}')
