import sqlite3
from random import choice

class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
            name TEXT,
            frags INTEGER,
            score_points INTEGER
        )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()

    def get(self, que='SELECT * FROM score ORDER BY score_points DESC, frags ASC,  name ASC '):
        return self.cur.execute(que).fetchall()



    def insert(self, name, frags, score):
        que_insert = f'''
        INSERT INTO score (name, frags,  score_points)
        VALUES ('{name}', {frags} ,{score})
        '''
        self.cur.execute(que_insert)
        self.con.commit()



    def __del__(self):
        self.con.close()




data_base = DataBase('game.sqlite')
pool_name = ('Azer', 'Kushyan', 'Edgar', 'Ross')
pool_score_points = ('15', '23', '36', '6')
pool_frags = tuple(range(2,6))

for i in range(10):
    name_insert = choice(pool_name)
    score_points_insert = choice(pool_score_points)
    frags_insert = choice(pool_frags)
    data_base.insert(name_insert, score_points_insert, frags_insert)
data = data_base.get()
for line in data:
    print(line)