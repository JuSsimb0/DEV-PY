import json
import os

def task() -> float:
    count = 0
    filename = "input.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        count = sum(cur_dict['score'] * cur_dict['weight'] for cur_dict in data)

        return round(count, 3)


print(task())
