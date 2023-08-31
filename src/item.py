import os, csv
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return str(self.__name)

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            print('Длина наименования товара превышает 10 символов')
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        path_end = path.split('/')
        file = Path(__file__).parent.parent.joinpath(path_end[0]).joinpath(path_end[1])
        with open(os.path.join(file), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all.append(cls(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(number):
        return int(float(number)//1)
