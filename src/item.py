import os, csv
from pathlib import Path
from src.exeptions import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    PATH_CVS = os.path.join('..', 'src', 'items.csv')
    # path_end = PATH_CVS.split('/')
    # file = Path(__file__).parent.parent.joinpath(path_end[0]).joinpath(path_end[1])
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return str(self.name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price_product = self.price * self.quantity
        return total_price_product

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        discont_prise = self.price * self.pay_rate
        return discont_prise

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(os.path.join(cls.PATH_CVS), newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if None in row.values():
                        raise InstantiateCSVError
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(number):
        return int(float(number)//1)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise AssertionError('Складывать можно только экземпляры классов Item или Phone.')
