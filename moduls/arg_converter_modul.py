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