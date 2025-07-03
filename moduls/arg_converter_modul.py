def arg_converter(arg):
    # Функция для коонвертирования аргументов в удобный вид
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