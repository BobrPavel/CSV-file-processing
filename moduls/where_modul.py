from moduls.arg_converter_modul import arg_converter


def where_func(list_of_dicts, arg):
    # Функция фильтрации (>, <, =)

    try:
        
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
                if float(item.get(column)) > float(value):
                    output_list.append(item)

            elif operator == "<":
                if float(item.get(column)) > float(value):
                    output_list.append(item)

        return output_list

    except Exception:
        print("Проверьте корректность ввода команды")


