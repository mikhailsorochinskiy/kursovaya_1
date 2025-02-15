import json
import os

from src.operations import get_operations_from_excel
from src.stocks_and_currency import get_currency_rate, get_stocks_rate
from src.utils import get_cards_information, get_sentence, get_top_transactions, time_period

PATH_TO_FILE = os.path.dirname(__file__)
data = get_operations_from_excel(os.path.join(PATH_TO_FILE, 'data/operations.xlsx'))


def main_page(date: str) -> json:
    """Функция принимает дату и возвращает json-ответ с информацией для главной страницы сайта"""
    hello_message = get_sentence(date)
    filtered_data = time_period(data, date)
    cards_list = get_cards_information(filtered_data)
    top_transactions = get_top_transactions(filtered_data)
    currency_rates = get_currency_rate()
    stocks_rates = get_stocks_rate()
    result = {
        "greeting": hello_message,
        "cards": cards_list,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        'stock_prices': stocks_rates
    }
    return json.dumps(result, ensure_ascii=False, indent=4)
