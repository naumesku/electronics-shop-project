from tests.fixture import phone_exempl


def test_repr(phone_exempl):
    assert repr(phone_exempl) == "Phone('Название', 100000, 5, 1)"

def test_number_of_sim(phone_exempl):
    assert phone_exempl.number_of_sim == 1
