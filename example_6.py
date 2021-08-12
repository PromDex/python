# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ —# характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

#goods = []
#features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
#analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
#num = 0
#feature_ = None
#control = None
#
#while True:
#    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
#    if control == 'Q':
#        break
#    num += 1
#    if control == 'A':
#        print(f'\n Current analytics \n {"-" * 30}')
#        for key, value in analytics.items():
#            print(f'{key[:25]:>30}: {value}')
#            print("-" * 30)
#    for f in features.keys():
#        feature_ = input(f'Input feature "{f}"')
#        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
#        analytics[f].append(features[f])
#    goods.append((num, features))

# goods = int(input("Введите количество товара "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
#                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
#    my_list.append((n, my_dict))
#    n += 1
#    my_analys = dict(
#        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
#         'ед': my_dict.get('ед')})
# print(my_list)
# print(my_analys)
#
# Евгений Евтушенко, [10.08.21 00:41]
#
# ‘’’
# def print_menu():
#     """Вывводит меню на экран"""
#     print('1. Внести данные\n2. Вывести данные\n3.Выход')
#
#
# def create_new_entry(fields):
#     """Создает новую запись
#     input args: fields - ('name', 'age', ....) - список полей в записи
#     return - {'name': 'Tom', age: 56, ...} - dict - новая запись"""
#
#     entry = {}
#     for field in fields:
#     entry[field] = input(f'Введет значение поля {field} - ')
#     return entry
#
#
# def show_data(database):
#     """Выводит данные на экран"""
#     for entry in database:
#         print(entry)
#
# def main():
#     database = []
#     data_fields = ('name', 'age', 'income')
#
#     while True:
#         print_menu()
#         change = input('Выберите пункт меню - ')
#         if change == '1':
#             database.append(create_new_entry(fields=data_fields))
#
#         elif change == '2':
#             show_data(database)
#
#         elif change == '3':
#             break
#
#         else:
#             print('Выберите верный пункт меню')
#
# main()
# ‘’’