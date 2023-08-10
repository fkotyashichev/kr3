from func import get_time, get_transfer_amount_with_currency, get_from_where_to_where, load_executed_date


def main():
    operations = load_executed_date('operations.json')
    for operation in operations:
        line1 = f"{get_time(operation)} {operation['description']}"
        line2 = get_from_where_to_where(operation)
        line3 = get_transfer_amount_with_currency(operation)
        print(f'{line1}\n{line2}\n{line3}\n')


if __name__ == "__main__":
    main()
