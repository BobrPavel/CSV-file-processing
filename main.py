import argparse

from moduls.file_open_modul import file_open
from moduls.where_modul import where_func
from moduls.agregate_modul import aggregate_func
from moduls.output_modul import output_func



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--file", type=str, help="Ввод пути к файлу", required=True
    )
    parser.add_argument(
        "--where", type=str, help="Ввод параметров фильтрации", required=False
    )
    parser.add_argument(
        "--aggregate", type=str, help="Ввод параметров агрегации", required=False
    )

    args = parser.parse_args()
    
    if args.file:
        list_of_dicts = file_open(args.file)
    
        if args.where:
            list_of_dicts = where_func(list_of_dicts, args.where)
    
        if args.aggregate:
            list_of_dicts = aggregate_func(list_of_dicts, args.aggregate)
    
        output_func(list_of_dicts)
