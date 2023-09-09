import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard

@pytest.fixture
def phone_exempl():
    """Экземпляр класса Phone для теста"""
    return Phone("Название", 100_000, 5, 1)

@pytest.fixture
def item_exempl():
    """Экземпляр класса Item для теста"""
    return Item("Название", 1, 5)

@pytest.fixture
def keyboard_exempl():
    """Экземпляр класса Keyboard для теста"""
    return Keyboard("Defender", 2000, 5)

class NoItem:
    """
    Класс для тестов.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
