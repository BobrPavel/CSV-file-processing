from moduls.arg_converter_modul import arg_converter


def aggregate_func(list_of_dicts, arg):
    # Функция агрегации (min, max, avg)
    try:

        output_list = []
        items_list = []

        normal_arg_list = arg_converter(arg)

        column = normal_arg_list[0]
        value = normal_arg_list[2]

        for item in list_of_dicts:
            items_list.append(float(item.get(column)))

        if value == "max":
            output_list = {"max": max(items_list)}
        elif value == "min":
            output_list = {"min": min(items_list)}
        elif value == "avg":
            output_list = {"avg": round(sum(items_list) / len(items_list), 2)}
        else:
            print("Проверьте корректность ввода команды")

        list_of_dicts = []
        list_of_dicts.append(output_list)

        return list_of_dicts

    except Exception:
        print("Проверьте корректность ввода команды")

    