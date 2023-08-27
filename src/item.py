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
        self.__name = name
        self.price = price
        self.quantity = quantity


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
        self.price *= self.pay_rate


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(os.path.join('..', path), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # item = cls(row['name'], row['price'], row['quantity'])
                # cls.all.append(item)
                cls.all.append(cls(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(number):
        return int(float(number)//1)
