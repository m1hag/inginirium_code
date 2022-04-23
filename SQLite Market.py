import sqlite3
from random import choice

class Users:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('users')

    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cash INTEGER,
            year INTEGER
        )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()

    def get(self, que='SELECT * FROM users'):
        return self.cur.execute(que).fetchall()

    def get_old_users(self, que= 'SELECT * FROM users ORDER BY year ASC limit 3'):
        return self.cur.execute(que).fetchall()

    def delete_users(self, name):
        que_insert = f'''
        DELETE FROM users where name = '{name}'
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def add_money(self, id,money):
        que_insert = f'''
        UPDATE users set cash = cash + {money} where id = {id}
        '''
        self.cur.execute(que_insert)
        self.con.commit()





    def insert(self, name ,cash ,year):
        que_insert = f'''
        INSERT INTO users (name, cash, year)
        VALUES ('{name}', {cash}, {year})
        '''
        self.cur.execute(que_insert)
        self.con.commit()



    def __del__(self):
        self.con.close()




users_base = Users('market.sqlite')
#users_base.insert('govnar4ik', 5000, 2006)
#users_base.insert('term1x', 3000,2006)
#users_base.insert('m1hag.', 10000,2005)




pool_name = ('m1hag', 'term1x', 'govnar', 'obamrus2006')
pool_cash = (tuple (range(1000,7000)))
pool_year = (tuple(range(2010,2022)))
users_base.add_money(18,533)


#for i in range(10):
#    name_insert = choice(pool_name)
#    pool_cash_insert = choice(pool_cash)
#   year_insert = choice(pool_year)
#   users_base.insert(name_insert, pool_cash_insert, year_insert)
data = users_base.get()
for line in data:
    print(line)