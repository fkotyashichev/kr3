from func import load_executed_date
from func import get_time
from func import get_from_where_to_where
from func import get_transfer_amount_with_currency
import pytest


@pytest.fixture
def array_fixture():
    date = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]
    return date


def test_load_executed_date():
    assert len(load_executed_date('../operations.json')) == 5


def test_get_time(array_fixture):
    assert get_time(array_fixture[0]) == '26.08.2019 Перевод организации'
    assert get_time(array_fixture[1]) == '03.07.2019 Перевод организации'
    assert get_time(array_fixture[3]) == '04.04.2019 Перевод со счета на счет'


def test_get_from_where_to_where(array_fixture):
    assert get_from_where_to_where(array_fixture[0]) == 'Maestro 1596 83** **** 5199 -> Счет **9589'
    assert get_from_where_to_where(array_fixture[1]) == 'MasterCard 7158 30** **** 5199 -> Счет **5560'
    assert get_from_where_to_where(array_fixture[3]) == 'Счет **8542 -> Счет **4188'


def test_get_transfer_amount_with_currency(array_fixture):
    assert get_transfer_amount_with_currency(array_fixture[0]) == '31957.58 руб.'
    assert get_transfer_amount_with_currency(array_fixture[1]) == '8221.37 USD'
    assert get_transfer_amount_with_currency(array_fixture[3]) == '79114.93 USD'
