import json
import os

def task() -> float:
    count = 0
    filename = "input.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        for cur_dict in data:
            count += cur_dict['score'] * cur_dict['weight']

        return round(count, 3)


print(task())
