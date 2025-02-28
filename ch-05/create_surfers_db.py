import sqlite3


def create_db():
    db = sqlite3.connect("surfersDB.sdb")
    cursor = db.cursor()
    cursor.execute("""create table if not exists surfers
    (id integer primary key autoincrement,
                   name text,
                   country text,
                   average real,
                   board text,
                     age integer)""")

    db.commit()
    db.close()


def find_surfer_by_id(s_id):
    # Ready baked code
    db = sqlite3.connect("surfersDB.sdb")

    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == s_id:
            print("ID is " + str(row['id']))
            print("Name is " + row['name'])
            print("Country is " + row['country'])
            print("Average is " + str(row['average']))
            print("Board-type is " + row['board'])
            print("Age is " + str(row['age']))
    cursor.close()


# def leer_datos():
#     db = sqlite3.connect("surfersDB.sdb")
#     cursor = db.cursor()
#     cursor.execute("select * from surfers")
#     rows = cursor.fetchall()
#     for row in rows:
#         print("ID is " + str(row[0]))
#         print("Name is " + row[1])
#         print("Country is " + row[2])
#         print("Average is " + str(row[3]))
#         print("Board-type is " + row[4])
#         print("Age is " + str(row[5]))
#         print("")

#     cursor.close()
#     db.close()


def leer_text():
    with open("surfers_data.txt") as file:
        contenido = file.read()

    data = []
    for linea in contenido.split("\n"):
        # print(f'{linea=}')
        data.append(tuple(linea.split(";")))
        # data.append([(id, name, country, average, board, age)])

    return data


def insert_data(data):
    db = sqlite3.connect("surfersDB.sdb")
    cursor = db.cursor()
    cursor.executemany("""
                   insert into surfers (id, name, country, average, board, age) 
                   values (?, ?, ?, ?, ?, ?)""",
                       data)
    db.commit()
    db.close()


# create_db()
# datos = leer_text()
# insert_data(datos)
find_surfer_by_id(104)
