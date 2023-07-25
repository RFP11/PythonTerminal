from tabulate import tabulate as tb
import json
import os
from datetime import datetime as dt, date as dt_date
import calendar
from termcolor import colored


current_date = dt.now()
date_str = current_date.strftime('%Y %m %d')
year = int(current_date.strftime('%Y'))
month = int(current_date.strftime('%m'))
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


def set_calendar(year, month):
    cal_data = calendar.monthcalendar(year, month)
    month_name = current_date.strftime('%B')  # Get the full month name
    headers = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    calendar_data = []
    deadlines = set()

    # Collect all the deadlines for the current month
    for task in load_data():
        task_date = dt.strptime(task["Deadline"], "%Y %m %d").date()
        if task_date.year == year and task_date.month == month:
            deadlines.add(task_date.day)

    for week in cal_data:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                day_str = str(day)
                day_date = dt_date(year, month, day)
                if day_date == dt_date.today():
                    # Color the current date in red
                    day_str = colored(day_str, "red")
                elif day in deadlines:
                    # Color the deadline day in yellow
                    day_str = colored(day_str, "yellow")
                row.append(day_str)
        calendar_data.append(row)
    print(f"{month_name} {year}")  # Print the month name and year
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
    datas.append(new_task)
    save_data(datas)
    print("Entry added successfully.")
    input("Press Enter to continue...")
    clear_console()

while True:
    clear_console()
    print(date_str)
    print(f'Current month is {month}')
    set_calendar(year, month)
    display_subject_task()
    print("\n--- Log Progress Menu ---")
    print("1. Add Entry")
    print("2. Delete Entry")
    print("3. Update Entry")
    print("4. Exit")

    choices = input("Enter Your Choices (1-4): ")

    if choices == '1':
       add_new_task() 
    elif choices == '2':
        display_subject()
    elif choices == '3':
        display_subject()
    elif choices == '4':
        break
    else:
        print('Invalid choices')
    
