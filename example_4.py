# 4. Начните работу над проектом «Склад
# оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
# определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
# каждого типа оргтехники.

from datetime import datetime


class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        # ввод в словарь название оборудования, серийный номер и время поступления на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number: [equipment.title, self, t]})
        print('На склад ' + self.title + ' получено оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))

    def give_to_depot(self, equipment, other):
        # выдача оборудования из склада.
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title, other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)

    def list_equipments(self):
        print('На склад ' + self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада ' + self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))


class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(Office_equipment):
    def __init__(self, title, serial_number, print_velocity):
        Office_equipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title, serial_number, resolution):
        Office_equipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.resolution)


class Copier(Office_equipment):
    def __init__(self, title, serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.addit)


store1 = Depot('Main warehouse')
store2 = Depot('Small warehouse')

a = Printer('HP', 345678, 100)
b = Scanner('Epson', 123456, 4000)
c = Copier('Brother', 987654, 50)

print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)

store1.give_to_depot(a, store2)

store1.list_equipments()
store2.list_equipments()
