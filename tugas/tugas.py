from tabulate import tabulate as tb
import json
import os
from datetime import datetime as dt
import calendar


date = dt.now()
date_str = date.strftime('%Y %m %d')
year = int(date.strftime('%Y'))
month = int(date.strftime('%m'))
month_str = date.strftime('%B')

tugasFile = 'tugas.json'

def load_data():
    try:
        with open(tugasFile, 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []
    return data

def save_data(data):
    with open(tugasFile, 'w') as file:
        json.dump(data, file, indent=4)


def display_subject():
    subjects = ['Bahasa Indonesia', 'Bahasa Inggris', 'Bahasa Jepang', 'Bahasa Sunda', 'Matematika', 'Pendidikan Pancasila', 'PKK', 'PAI']
    print('Select Subject')
    print(tb(enumerate(subjects, start=1), headers=['ID', 'Name'], tablefmt='psql'))
    return subjects


def display_subject_task():
    datas = load_data()
    print(tb(datas, headers='keys', tablefmt='psql'))
    input("Press Enter to continue...")
    clear_console()


def set_calendar(year, month):
    cal_data = calendar.monthcalendar(year, month)
    headers = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    calendar_data = []  # Renamed 'table_data' to 'calendar_data'
    for week in cal_data:
        row = [str(day) if day != 0 else "" for day in week]
        calendar_data.append(row)  # Append rows to 'calendar_data', not 'cal_data'
    print(tb(calendar_data, headers=headers, tablefmt="grid"))


def clear_console():
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

def add_new_task():
    datas = load_data()
    subjects = display_subject()
    subject = int( input('Select subject ID: '))
    task = input('What the task about: ')
    print('Deadline format (YYYY MM DD)')
    deadline = input('When is the deadline: ')

    new_task = {
            'Subject': subjects[int((subject)-1)],
            'Task': task,
            'Added': date_str,
            'Deadline': deadline
            }
    print(new_task)
    input("Press Enter to continue...")
    clear_console()

while True:
    clear_console()
    print(date_str)
    print(f'Current month is {month_str}')
    set_calendar(year, month)
    print("\n--- Log Progress Menu ---")
    print("1. Add Entry")
    print("2. Delete Entry")
    print("3. Update Entry")
    print("4. Show Entries")
    print("5. Exit")

    choices = input("Enter Your Choices (1-5): ")

    if choices == '1':
       add_new_task() 
    elif choices == '2':
        display_subject()
    elif choices == '3':
        display_subject()
    elif choices == '4':
        display_subject_task()
    elif choices == '5':
        break
    else:
        print('Invalid choices')
    
