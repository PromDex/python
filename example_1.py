# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

in_name = input('Введите имя файла:')

my_list = []

while True:
    line = input('Введите строку в файл:')
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open(in_name, "w") as file_obj:
        file_obj.writelines(my_list)
