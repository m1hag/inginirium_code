import sqlite3

con = sqlite3.connect('school.sqlite')
cur = con.cursor()

que_insert = '''
SELECT surname, mark FROM class
WHERE surname = 'Соколов'   
'''

result = cur.execute(que_insert)
data = result.fetchall()
for line in data:
    print(line)

con.close()