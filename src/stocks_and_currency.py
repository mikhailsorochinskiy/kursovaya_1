import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")

PATH_TO_FILE = os.path.dirname(os.path.dirname(__file__))
PATH_TO_JSON_FILE = os.path.join(PATH_TO_FILE, 'user_settings.json')

stock_currency_dict = dict()


def get_currency_rate() -> dict:
    """Функция возвращает курс доллара и евро"""
    url_1 = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1"
    url_2 = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    payload = {}
    headers = {
      "apikey": API_KEY
    }
    response_eur = requests.request("GET", url_1, headers=headers, data=payload)
    response_usd = requests.request("GET", url_2, headers=headers, data=payload)
    result_eur = response_eur.json()["result"]
    result_usd = response_usd.json()["result"]
    result = {
      'EUR': result_eur,
      'USD': result_usd
    }
    stock_currency_dict['currency'] = [key for key in result.keys()]
    with open(PATH_TO_JSON_FILE, 'w+') as file:
        json.dump(stock_currency_dict, file, indent=4)
    return result


def get_stocks_rate() -> list[dict]:
    """Функция возвращает курс акций S&P500"""
    api_url_aapl = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format('AAPL')
    response_aapl = requests.get(api_url_aapl, headers={'X-Api-Key': API_KEY_STOCKS})
    api_url_amzn = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format('AMZN')
    response_amzn = requests.get(api_url_amzn, headers={'X-Api-Key': API_KEY_STOCKS})
    api_url_googl = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format('GOOGL')
    response_googl = requests.get(api_url_googl, headers={'X-Api-Key': API_KEY_STOCKS})
    api_url_msft = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format('MSFT')
    response_msft = requests.get(api_url_msft, headers={'X-Api-Key': API_KEY_STOCKS})
    api_url_tsla = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format('TSLA')
    response_tsla = requests.get(api_url_tsla, headers={'X-Api-Key': API_KEY_STOCKS})
    result = [{'stock': 'AAPL', 'price': response_aapl.json()['price']},
              {'stock': 'AMZN', 'price': response_amzn.json()['price']},
              {'stock': 'GOOGL', 'price': response_googl.json()['price']},
              {'stock': 'MSFT', 'price': response_msft.json()['price']},
              {'stock': 'TSLA', 'price': response_tsla.json()['price']}]
    stock_currency_dict['stocks'] = [stock['stock'] for stock in result]
    with open(PATH_TO_JSON_FILE, 'w+') as file:
        json.dump(stock_currency_dict, file, indent=4)
    return result
