import datetime


def get_sentence(date_str: str) -> str:
    """Функция принимает дату и возвращает приветствие"""
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        hour = date.hour
        if hour < 4:
            return 'Доброй ночи'
        elif hour < 12:
            return 'Доброе утро'
        elif hour < 17:
            return 'Добрый день'
        elif hour < 24:
            return 'Добрый вечер'
    except ValueError as e:
        print("Неправильный формат даты")
        raise e


def time_period(operations: list[dict], date_str: str) -> list[dict]:
    """Функция фильтрует по дате список транзакций (с 1 числа месяца до переданной даты)"""
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    filtered_data = []
    for operation in operations:
        current_date = datetime.datetime.strptime(operation.get('Дата операции'), '%d.%m.%Y %H:%M:%S')
        if current_date <= date and current_date.year == date.year and current_date.month == date.month:
            filtered_data.append(operation)
    return filtered_data


def get_cards_information(operations: list[dict]) -> list[dict]:
    """Функция принимает список словарей об операциях и возвращает список словарей с информацией о картах"""
    cards_list = []
    last_digits_list = list(set(transaction.get('Номер карты')[-4:] for transaction in operations
                                if type(transaction.get('Номер карты')) is not float))
    for last_digits in last_digits_list:
        total_spent = abs(sum([transaction.get('Сумма операции') for transaction in operations
                               if transaction.get('Сумма операции') < 0 and
                               transaction.get('Номер карты') == '*' + last_digits]))
        cards_list.append({
            'last_digits': last_digits,
            'total_spent': total_spent,
            'cashback': round(total_spent / 100, 2)
        })
    return cards_list


def get_top_transactions(operations: list[dict]) -> list[dict]:
    """Функция принимает список словарей об операциях и возвращает список с 5 словарями самых дорогих покупок"""
    sorted_data = sorted(operations, key=lambda x: abs(x.get('Сумма операции')), reverse=True)
    result = []
    k = 0
    for transaction in sorted_data:
        if transaction.get('Статус') == 'OK':
            result.append({
                'date': transaction.get('Дата операции').split()[0],
                'amount': transaction.get('Сумма операции'),
                'category': transaction.get('Категория'),
                'description': transaction.get('Описание')
            })
            k += 1
        if k == 5:
            break
    return result
