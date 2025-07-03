from tabulate import tabulate


def output_func(list_of_dicts):
    # The output function to the table
    print(tabulate(list_of_dicts, headers="keys", tablefmt="grid"))