"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    delta_1 = timedelta(days=1)
    yesterday = dt_now - delta_1
    delta_30 = timedelta(days=30)
    ago_30_days = dt_now - delta_30
    print(f'Вчера: {yesterday}\nСегодня: {dt_now}\n30 дней назад: {ago_30_days}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
#    imp_str =  "01/01/25 12:10:03.234567"
    dt_imp_str = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt_imp_str

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
