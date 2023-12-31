# TODO импортировать необходимые молули
import csv
import json
import os

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    if os.path.exists(INPUT_FILENAME):
        with open(INPUT_FILENAME, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='\n')
            data = [row for row in csv_reader]
            # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4) # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
