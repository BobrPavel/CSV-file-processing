from moduls.arg_converter_modul import arg_converter


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