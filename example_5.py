# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не оргтехника")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Scanner', *args)


class Copier(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Copier', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("HP", "XP-400"))
    storage.add(Scanner("Epson", "5367-AD"))
    storage.add(Copier("Brother", "B779"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел 3')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)
