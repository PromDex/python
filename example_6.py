# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# 1 Вариант
in_word = input('Введите несколько латинских строчных слов через пробел: ')


def int_func(a):
    return a.title()


print('Результат 1:', int_func(in_word))


# 2 Вариант


def my_func(a):
    sep_word = a.split(' ')
    total = []
    for i in sep_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print('Результат 2:', (' '.join(my_func(in_word))))
