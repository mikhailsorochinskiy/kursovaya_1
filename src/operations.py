import pandas as pd


def get_operations_from_excel(file_path: str) -> list[dict]:
    """Функция принимает excel файл и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка: {e}")
        raise e
