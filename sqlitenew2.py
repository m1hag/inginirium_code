import sqlite3

con = sqlite3.connect('school.sqlite')
cur = con.cursor()

que_insert = '''
INSERT INTO class (name,surname,mark) VALUES
    ('Азер', 'Кушан', 3),
    ('Серик', 'Жаров', 4),
    ('Мегамотикер', 'Гадаров', 5),
    ('Обам', 'Скилко', 2)
'''

cur.execute(que_insert)
con.commit()

con.close()