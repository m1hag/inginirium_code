import tkinter
from tkinter import ttk
import sqlite3



#def db_resp(req):
 #   con=sqlite3.connect('market.sqlite')
  #  cur=con.cursor
   # return cur.execute(req).fetchall()




def fill_table(user_table, data):
    for i in range(len(data)):
        user_table.insert(parent='', index = 'end', iid=i, text= '',
        values = data[i])








#def button_click_find(user_table, data):
#    a= getEntry.get()
#    print(a)
#    fill_table(user_table, data)

master = tkinter.Tk()
def getEntry():
    data = ([(1, 'govnar4ik', 5000, 2006), (2, 'term1x', 3000, 2006), (3, 'm1hag.', 10000, 2005),
             (4, 'Ник на русском', 7500, 2006), (5, 'dnq', 12500, 2003)])
    res = myEntry.get()
    que='''{}'''
    #data = db_resp(que.format(res))
    print(res)
    fill_table(user_table,data)
myEntry= tkinter.Entry (master,width=40)
myEntry.pack(pady=20)
btn = tkinter.Button(master, height = 1, width = 10,text='Read', command = getEntry)
btn.pack()



master.geometry('800x800')
frame = tkinter.Frame(master)
frame.pack()
user_table = ttk.Treeview(frame)
user_table['columns'] = ('id', 'name', 'cash', 'year')


user_table.column('#0', width=0)
user_table.heading('id', text='ID')
user_table.heading('name', text='Name')
user_table.heading('cash', text='Cash')
user_table.heading('year', text='Year')





#search= ''
#search_entry = tkinter.Entry(master,width=40)
#search_entry.pack()
#search_button = tkinter.Button(text='Сюда жми', width='10', height ='3', command=button_click_find(user_table,data))


many_screen=ttk.Notebook(master)
f1=tkinter.Frame(many_screen)
f2=tkinter.Frame(many_screen, height=400, width = 400)

many_screen.add(f1,text='Users')
many_screen.add(f2,text='Skins')




WIDTH = 1000
HEIGHT = 1000

canvas = tkinter.Canvas(master, bg = 'Gray',
                        width= WIDTH, height=HEIGHT)

canvas.pack()
#search_button.pack()
user_table.pack()
many_screen.pack()
master.mainloop()
