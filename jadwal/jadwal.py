from tabulate import tabulate as tb
import os
from datetime import datetime

dt = datetime.now()

day = dt.strftime('%A')

if day == 'Monday':
    hari = 'Senin'
elif day == 'Tuesday':
    hari = 'Selasa'
elif day == 'Wednesday':
    hari = 'Rabu'
elif day == 'Thursday':
    hari = 'Kamis'
elif day == 'Friday':
    hari = 'Jumat'
else:
    hari = 'Liburr'


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_console()
jadwal = {
        'Senin': ['Bahasa Inggris', 'PAI', 'Pendidikan Pancasila', 'Bahasa Jepang'],
        'Selasa': ['Bahasa Indonesia', 'Matematika', 'PAI', 'Bahasa Sunda'],
        'Rabu': ['PKK'],
        'Kamis': ['Bahasa Jepang', 'Bahasa Sunda', 'Matematika'],
        'Jumat': ['Bahasa Inggris', 'Pendidikan Pancasila', 'Bahasa Indonesia']
        }
print(f'Hari ini hari: {hari} ')
print(tb(jadwal, headers='keys', tablefmt='psql'))
