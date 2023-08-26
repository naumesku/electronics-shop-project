"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000




def test_apply_discount():
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000.0