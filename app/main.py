import csv
import argparse
from tabulate import tabulate


parser = argparse.ArgumentParser()

parser.add_argument(
    "--file", type=str, help="Enter the path to the file", required=True
)
parser.add_argument(
    "--where", type=str, help="Enter the filter parameter", required=False
)
parser.add_argument(
    "--aggregate", type=str, help="Enter a parameter for aggregation", required=False
)

args = parser.parse_args()


def file_open(file_name):
    # csv file reading function
    file_content = []
    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")

        for line in reader:
            file_content.append(dict(line))

        return file_content


def arg_converter(arg):
    # The function is a converting argument in a convenient list of three elements
    list_of_all_symbols = list(arg)
    output_list = []

    if ">" in list_of_all_symbols:
        output_list = arg.split(">")
        output_list.insert(1, ">")

    elif "<" in list_of_all_symbols:
        output_list = arg.split("<")
        output_list.insert(1, "<")

    elif "=" in list_of_all_symbols:
        output_list = arg.split("=")
        output_list.insert(1, "=")

    return output_list


def where_func(list_of_dicts, arg):
    # Filter function (>, <, =)
    output_list = []

    normal_arg_list = arg_converter(arg)

    column = normal_arg_list[0]
    operator = normal_arg_list[1]
    value = normal_arg_list[2]

    for item in list_of_dicts:
        if operator == "=":
            if item.get(column) == value:
                output_list.append(item)

        elif operator == ">":
            if item.get(column) > value:
                output_list.append(item)

        elif operator == "<":
            if item.get(column) < value:
                output_list.append(item)

    return output_list


def aggregate_func(list_of_dicts, arg):
    # Aggregate function (min, max, avg)
    output_list = []
    items_list = []

    normal_arg_list = arg_converter(arg)

    column = normal_arg_list[0]
    value = normal_arg_list[2]

    for item in list_of_dicts:
        items_list.append(float(item.get(column)))

    if value == "max":
        output_list = {"max": max(items_list)}

    if value == "min":
        output_list = {"min": min(items_list)}

    if value == "avg":
        output_list = {"avg": round(sum(items_list) / len(items_list), 2)}

    list_of_dicts = []
    list_of_dicts.append(output_list)

    return list_of_dicts


def output_func(list_of_dicts):
    # The output function to the table
    print(tabulate(list_of_dicts, headers="keys", tablefmt="grid"))


if args.file:
    list_of_dicts = file_open(args.file)

    if args.where:
        list_of_dicts = where_func(list_of_dicts, args.where)

    if args.aggregate:
        list_of_dicts = aggregate_func(list_of_dicts, args.aggregate)

    output_func(list_of_dicts)
