from unittest.mock import MagicMock, patch

from src.stocks_and_currency import get_currency_rate, get_stocks_rate


@patch("requests.request")
def test_get_currency_rate(mock_result):
    mock_result_eur = MagicMock()
    mock_result_eur.json.return_value = {'result': 100}
    mock_result_usd = MagicMock()
    mock_result_usd.json.return_value = {'result': 98}
    mock_result.side_effect = [mock_result_eur, mock_result_usd]
    assert get_currency_rate() == {
      'EUR': 100,
      'USD': 98
    }


@patch("requests.get")
def test_get_stocks_rate(mock_result):
    mock_result.return_value.json.return_value = {'price': 100}
    assert get_stocks_rate() == [{'stock': 'AAPL', 'price': 100},
                                 {'stock': 'AMZN', 'price': 100},
                                 {'stock': 'GOOGL', 'price': 100},
                                 {'stock': 'MSFT', 'price': 100},
                                 {'stock': 'TSLA', 'price': 100}]
