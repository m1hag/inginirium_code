import tkinter
from tkinter import ttk


def fill_table(user_table, data):
    for i in range(len(data)):
        user_table.insert(parent='', index = 'end', iid=i, text= '',
        values = data[i])




master = tkinter.Tk()
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
data = ([(1, 'govnar4ik', 5000, 2006), (2, 'term1x', 3000, 2006), (3, 'm1hag.', 10000, 2005), (4, 'Ник на русском', 7500, 2006), (5, 'dnq', 12500, 2003)])

search_button = tkinter.Button(text='Сюда жми', width='10', height ='3')
search_button.config(command=fill_table(user_table, data))

search= ''
search_entry = tkinter.Entry(textvariable=search)

#fill_table(user_table, data)

search_entry.pack()
search_button.pack()
user_table.pack()






WIDTH = 1000
HEIGHT = 1000

canvas = tkinter.Canvas(master, bg = 'Gray',
                        width= WIDTH, height=HEIGHT)



canvas.pack()
master.mainloop()