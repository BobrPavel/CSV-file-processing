from tabulate import tabulate


def output_func(list_of_dicts):
    # Функция вывода в таблицу
    print(tabulate(list_of_dicts, headers="keys", tablefmt="grid"))