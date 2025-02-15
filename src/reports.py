import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta

from src.decorators import decorator


@decorator
def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """Функция принимает объект датафрейм и возвращает новый датафрейм со средними тратами по дням недели за последние
    3 месяца от переданной даты"""
    if date is None:
        end_date = datetime.datetime.today()
    else:
        end_date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    start_date = end_date - relativedelta(months=3)
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'],
                                                   format='%d.%m.%Y %H:%M:%S', errors='coerce')
    filtered_df = transactions.loc[(transactions['Дата операции'] >= start_date)
                                   & (transactions['Дата операции'] <= end_date)].copy()
    filtered_df['weekday'] = filtered_df['Дата операции'].dt.weekday
    sorted_by_weekday = filtered_df.groupby('weekday')
    result = sorted_by_weekday['Сумма операции с округлением'].mean()
    return result


data = pd.read_excel('../data/operations.xlsx')

if __name__ == '__main__':
    spending_by_weekday(data, '10.03.2021 12:12:12')
