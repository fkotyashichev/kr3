import datetime
import json


def load_executed_date(filename):
    """Функция загрузки выполненных операций из файла"""
    with open(filename, 'r', encoding='UTF-8') as f:
        all_date = json.load(f)

    # Выбираем выполненные операции
    good_date = []
    for transaction in all_date:
        if 'from' not in transaction:
            continue
        elif transaction['state'] == 'EXECUTED':
            good_date.append(transaction)

    # Сортируем по дате
    good_date = sorted(good_date, key=lambda x: x['date'])
    return good_date[-5:]


def get_time(date):
    """ВЫвод даты в нужном формате"""
    pass


def get_from_where_to_where(date):
    """Вывод Откуда и Куда прошла операция
    в замаскированном формате"""
    pass


def get_transfer_amount_with_currency(date):
    """Вывод Суммы перевод и валюты"""
    pass
