import pytest

from src.utils import get_cards_information, get_sentence, get_top_transactions, time_period

transactions = [
    {
        "Дата операции": "17.07.2019 15:01:15",
        "Дата платежа": "19.07.2019",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -27.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -27.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": 0,
        "Категория": "Дом и ремонт",
        "MCC": 5200.0,
        "Описание": "OOO Nadezhda",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 27.0,
    },
    {
        "Дата операции": "14.07.2019 16:30:10",
        "Дата платежа": "18.07.2019",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -49.8,
        "Валюта операции": "RUB",
        "Сумма платежа": -49.8,
        "Валюта платежа": "RUB",
        "Кэшбэк": 0,
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "SPAR",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 49.8,
    },
]


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2021-12-12 23:23:23", "Добрый вечер"),
        ("2021-12-12 15:23:23", "Добрый день"),
        ("2021-12-12 11:23:23", "Доброе утро"),
        ("2021-12-12 02:23:23", "Доброй ночи"),
    ],
)
def test_get_sentence(date, expected):
    assert get_sentence(date) == expected


def test_get_sentence_negative():
    with pytest.raises(ValueError):
        get_sentence("2021:12:01")


@pytest.fixture()
def return_data_time_period():
    return [
        {
            "Дата операции": "14.07.2019 16:30:10",
            "Дата платежа": "18.07.2019",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -49.8,
            "Валюта операции": "RUB",
            "Сумма платежа": -49.8,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "SPAR",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 49.8,
        }
    ]


def test_time_period(return_data_time_period):
    assert time_period(transactions, "2019-07-15 23:23:23") == return_data_time_period


def test_get_cards_information():
    assert get_cards_information(transactions) == [{"last_digits": "7197", "total_spent": 76.8, "cashback": 0.77}]


def test_get_top_transactions():
    assert get_top_transactions(transactions) == [
        {"date": "14.07.2019", "amount": -49.8, "category": "Супермаркеты", "description": "SPAR"},
        {"date": "17.07.2019", "amount": -27.0, "category": "Дом и ремонт", "description": "OOO Nadezhda"},
    ]
