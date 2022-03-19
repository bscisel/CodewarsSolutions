import json


def read_numbers_from_file(file_name: str):
    with open(file_name) as file:
        return json.load(file)


def parse_to_int(string: str):
    numbers = read_numbers_from_file("numbers.json")
    split = string.replace(' and ', ' ').replace('-', ' ').split()
    number = group = 0
    for word in split:
        if word in numbers['0-90']:
            group += numbers['0-90'][word]
        elif word == "hundred":
            group *= 100
        elif word in numbers['100-']:
            group *= numbers['100-'][word]
            number += group
            group = 0
    return number + group
