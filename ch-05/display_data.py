from pathlib import Path
import sqlite3


def find_details_in_csv_file(id):
    file = Path('rsa_data.csv')
    dir = Path('ch-05')
    file_path = dir / file

    with open(file_path) as file:
        s = {}
        s['id'] = None
        for line in file:
            if line.startswith(str(id)):
                (s['id'], s['name'], s['country'], s['average'],
                 s['board'], s['age']) = line.strip().split(';')
    return s


def find_details(id2find):
    # Ready baked code
    file = Path('surfersDB.sdb')
    dir = Path('ch-05')
    file_path = dir / file

    db = sqlite3.connect(file_path)

    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()

    s = {}
    s['id'] = None

    for row in rows:
        if row['id'] == id2find:
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
    return s


def print_details(s, id):
    if s['id'] is None:
        print(f'Surfer {id} not found')
    else:
        print(s['id'], s['name'], s['country'],
              s['average'], s['board'], s['age'])


def testing_find_details():
    for id in range(101, 109):
        data = {}
        data = find_details(id)
        print_details(data, id)


testing_find_details()
