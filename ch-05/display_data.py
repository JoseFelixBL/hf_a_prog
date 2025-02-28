from pathlib import Path


def find_details(id):
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
