from tabulate import tabulate as tb
import json
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


def load_data():
    try:
        with open('kurikulum.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []
    return data

datas = load_data()
print('Kurikulum Semester 1')
print(tb(datas, headers='keys', tablefmt='psql'))
