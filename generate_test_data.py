import csv
import json
import pandas as pd

def csv_to_json(csv_file, json_file):
    """
    Преобразует CSV-файл в JSON-файл.

    Args:
        csv_file (str): Путь к CSV-файлу.
        json_file (str): Путь к выходному JSON-файлу.
    """

    # Читаем CSV-файл в DataFrame
    df = pd.read_csv(csv_file)

    # Преобразуем DataFrame в список словарей
    data = df.to_dict('records')

    # Записываем данные в JSON-файл
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


csv_file = 'data/train.csv'
json_file = 'my_data.json'
csv_to_json(csv_file, json_file)






# Пример использования
import json

def convert_json_types(json_file):
    """
    Преобразует числовые строки в JSON-файле в числовые типы.

    Args:
        json_file (str): Путь к JSON-файлу.
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    for key, value in data.items():
        try:
            # Пытаемся преобразовать значение в float
            data[key] = float(value)
            # Если преобразование успешно, проверяем, является ли число целым
            if data[key].is_integer():
                data[key] = int(data[key])
        except ValueError:
            # Если преобразование не удалось, оставляем значение как строку
            pass

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
