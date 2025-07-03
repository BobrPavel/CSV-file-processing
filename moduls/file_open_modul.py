import csv

def file_open(file_name):
    # Функция чтения csv файлов
    try:
        file_content = []
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")

            for line in reader:
                file_content.append(dict(line))

            return file_content
    except FileNotFoundError:
        print("Проверьте существует ли файл и правильность ввода его названия")

