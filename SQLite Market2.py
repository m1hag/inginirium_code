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

class Skin:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('skin')

    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quality Integer,
            price Float,
            rarity Text,
            stattrack Boolean
        )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()

    def get(self, que='SELECT * FROM skin'):
        return self.cur.execute(que).fetchall()

    def get_some_rarity(self, rarity):
        que = f'''SELECT * from skin where rarity =  ('{rarity}') '''
        return self.cur.execute(que).fetchall()

    def delete_skin(self,name, quality):
        que_insert = f'''
            DELETE from skin where name = '{name}' and quality = {quality}'''
        self.cur.execute(que_insert)
        self.con.commit()

    def get_some_st(self, stattrack):
        que = f''' SELECT * from skin where stattrack = {stattrack}'''
        return self.cur.execute(que).fetchall()


    def insert(self, name , quality, price, rarity, stattrack):
        que_insert = f'''
        INSERT INTO skin (name, quality, price, rarity, stattrack)
        VALUES ('{name}', {quality}, {price}, '{rarity}', {stattrack})
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):
        self.con.close()

class Inventory:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('inventory')

    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            UserID INTEGER FOREIGH KEY,
            SkinID INTEGER FOREIGH KEY
        )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()
    def get(self, que='SELECT * FROM inventory'):
        return self.cur.execute(que).fetchall()

    def get_first_users(self, que='SELECT * FROM inventory ORDER BY UserID ASC'):
        return self.cur.execute(que).fetchall()

    def get_info_from_tables(self):
        que= '''SELECT 
        Inventory.ID as id,
        users.name as user_name,
        skin.name as skin_name
    From
        Inventory
    LEFT JOIN users
    on users.id = UserID
    LEFT JOIN skin
    on skin.id = SkinID;'''
        return self.cur.execute(que).fetchall()


    def insert(self, UserID, SkinID):
        que_insert = f'''
        INSERT INTO inventory (UserID, SkinID)
        VALUES ({UserID}, {SkinID} )
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):
        self.con.close()



users_base = Users('market.sqlite')
'''users_base.insert('govnar4ik', 5000, 2006)
users_base.insert('term1x', 3000,2006)
users_base.insert('m1hag.', 10000,2005)
users_base.insert('Ник на русском', 7500, 2006)
users_base.insert('dnq', 12500, 2003)'''

skin_base = Skin('market.sqlite')
'''skin_base.insert('AK-47 | Emerald Dragon', 5, 250, 'Засекреченное', True)
skin_base.insert('MAC-10 | Red Apple', 3, 4, 'Армейское', False)
skin_base.insert('M249 | Biden', 1, 1, 'Ширпотреб', False)
skin_base.insert('AK-47 | Putin', 5, 25000, 'Тайное', True)
skin_base.insert('P90 | Zelenskiy', 1, 2, 'Ширпотреб', False)
skin_base.insert('M4A1 | Green Kushyan', 4, 325, 'Запрещенное', True)
skin_base.insert('Shadow Daggers | Red Erik', 3, 450, 'Тайное', True)
skin_base.insert('M4A1-S | Hyper Beast', 5, 250.50, 'Тайное', True)
skin_base.insert('AWP | Kushyan Beast', 5, 700.39, 'Тайное', True)
skin_base.insert('Снежок | Белый воин', 5, 15000, 'Тайное', True)'''

inventory_base = Inventory('market.sqlite')
'''inventory_base.insert(3,4)
inventory_base.insert(1, 1)
inventory_base.insert(2, 7)
inventory_base.insert(5, 6)
inventory_base.insert(2,2)
inventory_base.insert(3,7)
inventory_base.insert(4,2)
inventory_base.insert(1,8)
inventory_base.insert(4,4)'''






#pool_name = ('m1hag', 'term1x', 'govnar', 'obamrus2006')
#pool_cash = (tuple (range(1000,7000)))
#pool_year = (tuple(range(2010,2022)))
#users_base.add_money(18,533)


#for i in range(10):
#    name_insert = choice(pool_name)
#    pool_cash_insert = choice(pool_cash)
#   year_insert = choice(pool_year)
#   users_base.insert(name_insert, pool_cash_insert, year_insert)
#data = users_base.get()
#data = skin_base.get()
data = inventory_base.get_info_from_tables()
#data = skin_base.get_some_rarity('Тайное')
#skin_base.delete_skin('AWP | Kushyan Beast', 5)

#data = skin_base.get_some_st(True)
for line in data:
    print(line)