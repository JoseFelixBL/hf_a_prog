def find_details(id):
    with open('rsa_data.csv') as file:
        s = {}
        s['id'] = None
        for line in file:
            if line.startswith(str(id)):
                (s['id'], s['name'], s['country'], s['average'],
                 s['board'], s['age']) = line.strip().split(';')
    return s


def print_details(s):
    if s['id'] is None:
        print(f'Surfer {id} not found')
    else:
        print(s['id'], s['name'], s['country'],
              s['average'], s['board'], s['age'])


for id in range(101, 109):
    data = {}
    data = find_details(id)
    print_details(data)
