import pytest
from tests.fixture import keyboard_exempl

def test_language(keyboard_exempl):
    keyboard_exempl.language
    assert keyboard_exempl.language == "EN"

def test_change_lang(keyboard_exempl):
    keyboard_exempl.change_lang()
    assert keyboard_exempl.language == "RU"
    keyboard_exempl.change_lang()
    assert keyboard_exempl.language == "EN"

    with pytest.raises(AttributeError):
        keyboard_exempl.language = "CH"
