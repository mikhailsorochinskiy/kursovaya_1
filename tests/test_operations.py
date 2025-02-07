import os
from unittest.mock import patch

import pytest

from src.operations import get_operations_from_excel

PATH_TO_FILE = os.path.dirname(__file__)

transactions = [{'Дата операции': '17.07.2019 15:01:15',
                 'Дата платежа': '19.07.2019',
                 'Номер карты': '*7197',
                 'Статус': 'OK',
                 'Сумма операции': -27.0,
                 'Валюта операции': 'RUB',
                 'Сумма платежа': -27.0,
                 'Валюта платежа': 'RUB',
                 'Кэшбэк': 0,
                 'Категория': 'Дом и ремонт',
                 'MCC': 5200.0,
                 'Описание': 'OOO Nadezhda',
                 'Бонусы (включая кэшбэк)': 0,
                 'Округление на инвесткопилку': 0,
                 'Сумма операции с округлением': 27.0},
                {'Дата операции': '16.07.2019 16:30:10',
                 'Дата платежа': '18.07.2019',
                 'Номер карты': '*7197',
                 'Статус': 'OK',
                 'Сумма операции': -49.8,
                 'Валюта операции': 'RUB',
                 'Сумма платежа': -49.8,
                 'Валюта платежа': 'RUB',
                 'Кэшбэк': 0,
                 'Категория': 'Супермаркеты',
                 'MCC': 5411.0,
                 'Описание': 'SPAR',
                 'Бонусы (включая кэшбэк)': 0,
                 'Округление на инвесткопилку': 0,
                 'Сумма операции с округлением': 49.8}]


@patch("pandas.read_excel")
def test_get_operations_from_excel(mock_reader):
    mock_reader.return_value.to_dict.return_value = transactions
    result = get_operations_from_excel(os.path.join(os.path.dirname(PATH_TO_FILE), 'data/operations.xlsx'))
    assert result == transactions


def test_get_transactions_from_excel_negative():
    with pytest.raises(FileNotFoundError):
        get_operations_from_excel("invalid_path")
