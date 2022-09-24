import sqlite3

class Users:
    def __init__(self, Snake,username):
        self.con = sqlite3.connect(Snake)
        self.cur = self.con.cursor()
        self.create_table('Users')
        self.name=username

    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
            name TEXT,
            score INTEGER
        )'''.format(table_name)
        self.cur_execute(que_create)
        self.con.commit()

    def get(self, que = 'SELECT * FROM Users'):
        return self.cur.execute(que).fetchall()

    def get_best_users(self, que = 'SELECT * FROM users ASC limit 3'):
        return self.cur.execute(que).fetchall()

    def insert(self, name,score):
        que_insert = f'''
        INSERT INTO Users (name,score)
        VALUES ('{name}, {score})
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):
        self.con.close()
