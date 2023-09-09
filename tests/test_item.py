"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from tests.fixture import phone_exempl, item_exempl, NoItem

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item3 = NoItem("Ноутбук", 20000, 5)

def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000.0
    assert item1.price == 10000

def test_name():
    item1.name = "абрикосабрикос"
    assert item1.name == "абрикосабр"
    item1.name = "абрикос"
    assert item1.name == "абрикос"

def test_instantiate_from_csv():
    item2.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5

def test_repr(item_exempl):
    assert repr(item_exempl) == "Item('Название', 1, 5)"

def test_str(item_exempl):
    assert str(item_exempl) == 'Название'

noitem1 = NoItem("Каша", 48, 5)
def test_add(item_exempl, phone_exempl):
    assert item_exempl + phone_exempl == 10
    with pytest.raises(AssertionError):
        item_exempl + noitem1
