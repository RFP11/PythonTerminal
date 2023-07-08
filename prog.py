import json
import os
from datetime import datetime as dt

from tabulate import tabulate


def load_data():
    try:
        with open('Progress.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []
    return data

def save_data(data):
    with open('Progress.json', 'w') as file:
        json.dump(data, file, indent=4)

def display_projects():
    projects = ['Upgradia', 'Virtuwed', 'Orbit', 'School', 'Osis']
    print('Available projects:')
    print(tabulate(enumerate(projects, start=1), headers=['ID', 'Project Name'], tablefmt='psql'))
    return projects

def display_entry():
    data = load_data()
    formatted_entries = []
    for i, entry in enumerate(data, start=1):
        formatted_entry = {
            'ID': i,
            'Date': entry['Date'],
            'Context': entry['Context'],
            'Progress': entry['Progress']
        }
        formatted_entries.append(formatted_entry)
    print(tabulate(formatted_entries, headers='keys', tablefmt='psql'))

def add_entry():
    data = load_data()
    projects = display_projects()

    project = input("Select a project: ")
    progress = input("Enter the progress: ")

    new_entry = {
        'Date': dt.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Context': projects[int(project)-1],
        'Progress': progress
    }

    data.append(new_entry)
    save_data(data)
    print("Entry added successfully.")
    input("Press Enter to continue...")
    clear_console()

def delete_entry():
    data = load_data()

    print("Current Entries:")
    display_entry()

    entry_number = input("Enter the entry number to delete: ")

    if entry_number.isnumeric():
        entry_number = int(entry_number)
        if entry_number > 0 and entry_number <= len(data):
            deleted_entry = data.pop(entry_number - 1)
            save_data(data)
            print("Deleted Entry:")
            print(tabulate([deleted_entry], headers='keys', tablefmt='psql'))
        else:
            print("Invalid entry number.")
    else:
        print("Invalid entry number format.")
    input("Press Enter to continue...")
    clear_console()

def update_entry():
    data = load_data()

    print("Current Entries:")
    display_entry()

    entry_number = input("Enter the entry number to update: ")

    if entry_number.isnumeric():
        entry_number = int(entry_number)
        if entry_number > 0 and entry_number <= len(data):
            entry = data[entry_number - 1]
            projects = display_projects()

            project = input("Select a new project (leave blank to keep current): ")
            progress = input("Enter the new progress (leave blank to keep current): ")

            if project:
                entry['Context'] = projects[int(project)-1]
            if progress:
                entry['Progress'] = progress

            entry['Date'] = dt.now().strftime("%Y-%m-%d %H:%M:%S")

            save_data(data)
            print("Entry updated successfully.")
        else:
            print("Invalid entry number.")
    else:
        print("Invalid entry number format.")
    input("Press Enter to continue...")
    clear_console()

def show_entries():
    data = load_data()
    if len(data) == 0:
        print("No entries found.")
    else:
        formatted_entries = []
        for i, entry in enumerate(data, start=1):
            formatted_entry = {
                'ID': i,
                'Date': entry['Date'],
                'Context': entry['Context'],
                'Progress': entry['Progress']
            }
            formatted_entries.append(formatted_entry)

        print("Current Entries:")
        print(tabulate(formatted_entries, headers='keys', tablefmt='psql'))
    input("Press Enter to continue...")
    clear_console()

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For other platforms (Linux, macOS)
        os.system('clear')

# Main menu
while True:
    clear_console()
    print("\n--- Log Progress Menu ---")
    print("1. Add Entry")
    print("2. Delete Entry")
    print("3. Update Entry")
    print("4. Show Entries")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        delete_entry()
    elif choice == '3':
        update_entry()
    elif choice == '4':
        show_entries()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    clear_console()
