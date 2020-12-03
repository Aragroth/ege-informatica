#########################################
#                                       #
# ШУТОЧНОЕ РЕШЕНИЕ. ТАК ДЕЛАТЬ НИ НАДА  #
#                                       #
#########################################

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS people (
        id integer PRIMARY KEY,
        gender char(3) NOT NULL,
        birth_year integer NOT NULL
    )
    """
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS pc_2_ch (
        id_pe INTEGER,
        id_ch INTEGER,
		FOREIGN KEY (id_pe) REFERENCES people,
		FOREIGN KEY (id_ch) REFERENCES people
    )
    """
)

people = [
    (1066,  'Ж', 1942),
    (1067,  'М', 1938),
    (1079,  'Ж', 1998),
    (1085,  'М', 1990),
    (1900,  'Ж', 2012),
    (1904,  'М', 1981),
    (1911,  'Ж', 1971),
    (1932,  'Ж', 2016),
    (1938,  'М', 1974),
    (1949,  'Ж', 1966),
    (1970,  'М', 1968),
    (1995,  'Ж', 2002),
    (917,   'М', 2003),
    (926,   'Ж', 1983),
    (941,   'Ж', 2010),
    (956,   'М', 1989),
]

many = [
    (1066,  1911),
    (1066,  1938),
    (1067,  1911),
    (1067,  1938),
    (1911,  1079),
    (1911,  941),
    (926,   1900),
    (1938,  1995),
    (1938,  917),
    (1949,  1995),
    (1949,  917),
    (1970,  1079),
    (1970,  941),
    (926,   1932),
    (1904,  1900),
    (1904,  1932),
]
 
cursor.executemany("INSERT INTO people VALUES (?,?,?)", people)
cursor.executemany("INSERT INTO pc_2_ch VALUES (?,?)", many)
conn.commit()


# Ищем людей, у которых матерям было меньше 28 лет на момент рождения
data = cursor.execute(
    """SELECT count(*)
    FROM people p
    JOIN pc_2_ch f ON p.id = f.id_ch
    JOIN people s ON f.id_pe = s.id
    WHERE s.gender = "Ж" AND  p.birth_year - s.birth_year  <= 28
    """
)

print(data.fetchall()[0][0])

