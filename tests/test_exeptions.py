import pytest, os
from src.exeptions import InstantiateCSVError
from src.item import Item


def test_InstantiateCSVError():
    Item.PATH_CVS = os.path.join('..', 'tests', 'test_cvs.cvs')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

def test_FileNotFoundError():
    Item.PATH_CVS = "nofile"
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
