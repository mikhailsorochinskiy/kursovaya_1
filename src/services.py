import re


def get_operations_tel_num(operations: list[dict]) -> list[dict]:
    """Функция возвращает список транзакций, в описании которых содержится номера телефонов"""
    pattern = r'\+7 \d{3} \d{3}-\d{2}-\d{2}'
    return [operation for operation in operations if re.search(pattern, operation.get('Описание'))]
