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
    my_date = date['date']
    my_date = my_date[:10]
    my_date = my_date.split('-')
    return '.'.join(reversed(my_date))


def get_from_where_to_where(date):
    """Вывод Откуда и Куда прошла операция
    в замаскированном формате"""
    from_ = date['from']
    from_ = from_.split(' ')
    info = from_[0]
    number = from_[-1]

    if info.lower().startswith("счет"):
        my_mask = '**'+number[-4:]
    else:
        my_mask = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    from_[-1] = my_mask

    to_ = date['to']
    to_ = to_.split(' ')
    info = to_[0]
    number = to_[-1]

    if info.lower().startswith("счет"):
        my_mask = '**'+number[-4:]
    else:
        my_mask = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    to_[-1] = my_mask
    return f"{' '.join(from_)} -> {' '.join(to_)}"


def get_transfer_amount_with_currency(date):
    """Вывод Суммы перевод и валюты"""
    return f"{date['operationAmount']['amount']} {date['operationAmount']['currency']['name']}"
