from src.item import Item

class MixinLeng():
    """
     Класс изменения и вывода языка
     """
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

class Keyboard(Item, MixinLeng):
    """
    Класс для товара 'клавиатура'
    """
    pass

