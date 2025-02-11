import json
import re


def get_operations_tel_num(operations: list[dict]) -> json:
    """Функция возвращает список транзакций, в описании которых содержится номера телефонов"""
    pattern = r'\+7 \d{3} \d{3}-\d{2}-\d{2}'
    result = [operation for operation in operations if re.search(pattern, operation.get('Описание'))]
    return json.dumps(result, ensure_ascii=False, indent=4)
