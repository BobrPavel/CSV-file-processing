# Обработка CSV файла
## Задача:
Написать скрипт для обработки CSV-файла, поддерживающий операции: 
- фильтрацию с операторами «больше», «меньше» и «равно»
- агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения

## Ссылка для плонировния проекта
```
git clon https://github.com/BobrPavel/CSV-file-processing.git

```
Убедитесь что у вас установлена библиотека tabulate
```
pip install tabulate

```


## Запуск:
```
python main.py --file ('путь к файлу')  

```
## Запуск с фильтрацией:
```
python main.py --file products.csv --where "price>199" 

```
## Запуск с фильтрацией и агрегацией:
```
python main.py --file products.csv --where "price=199" --aggregate "rating=max"

```
## Тестирование:
```
================================================= test session starts ===================================================
platform win32 -- Python 3.11.8, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\Павел\Desktop\Test_tusk
configfile: pytest.ini
collected 8 items

tests\test_agregate_modul.py .                                                                                      [ 12%] 
tests\test_arg_converter_modul.py .....                                                                             [ 75%]
tests\test_file_open_modul.py .                                                                                     [ 87%] 
tests\test_where_modul.py .                                                                                         [100%] 

==================================================== 8 passed in 0.09s ===================================================

```
