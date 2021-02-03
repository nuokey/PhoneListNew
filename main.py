import sqlite3
from tkinter import *

def contacts():
	global last_i, name, number, delete_contact, contact_was, label_list
	db = sqlite3.connect('data.db')
	cursor = db.cursor()
	# number_list = []
	# name_list = []
	# notes_list = []
	tele_list = []
	# for i in cursor.execute("SELECT number FROM phonelist"):
	# 	number_list.append(i[0])

	# for q in cursor.execute("SELECT name FROM phonelist"):
	# 	name_list.append(q[0])

	# for s in cursor.execute("SELECT notes FROM phonelist"):
	# 	notes_list.append(s[0])

	# for z in number_list:
	# 	tele_list.append()

	for i in cursor.execute("SELECT * FROM phonelist"):
		tele_list.append(i)

	if contact_was:
		for q in range(len(label_list)):
			label_list[q][0].destroy()
			label_list[q][1].destroy()
			label_list[q][2].destroy()

	label_list = []

	for i in range(len(tele_list)):
		name = Label(text = tele_list[i][0], bg = 'black', fg = 'white')
		number = Label(text = tele_list[i][1], bg = 'black', fg = 'white')
		notes = Label(text = tele_list[i][2], bg = 'black', fg = 'white')
		delete_contact = Button(text = 'x', command = lambda: contact_delete(name))

		name.place(x = 10, y = 30 + i * 30, width = 100, height = 20)
		number.place(x = 120, y = 30 + i * 30, width = 100, height = 20)
		notes.place(x = 230, y = 30 + i * 30, width = 100, height = 20)
		delete_contact.place(x = 335, y = 30 + i * 30, width = 20, height = 20)

		label_list.append((name, number, delete_contact))

		last_i = i
	
	contact_was = True

def contact_add():
	global last_i, plus_contact, enter_name, enter_number, enter_notes
	enter_name = Entry()
	enter_number = Entry()
	enter_notes = Entry()

	enter_name.place(x = 10, y = 30 + (last_i + 1) * 30, width = 100 ,height = 20)
	enter_number.place(x = 120, y = 30 + (last_i + 1) * 30, width = 100, height = 20)
	enter_notes.place(x = 230, y = 30 + (last_i + 1) * 30, width = 100, height = 20)

	plus_contact['text'] = 'S'
	plus_contact['command'] = contact_safe

def contact_delete(name):
	db = sqlite3.connect('data.db')
	cursor = db.cursor()
	a = name['text']
	cursor.execute(f'DELETE FROM phonelist WHERE name = "{a}"')
	print(a)
	db.commit()

	contacts()

def contact_safe():
	global last_i, plus_contact, enter_name, enter_number, enter_notes
	db = sqlite3.connect('data.db')
	cursor = db.cursor()
	cursor.execute(f'INSERT INTO phonelist VALUES ("{enter_name.get()}", "{enter_number.get()}", "{enter_notes.get()}")')
	db.commit()

	enter_name.destroy()
	enter_number.destroy()
	enter_notes.destroy()

	plus_contact['text'] = '+'
	plus_contact['command'] = contact_add

	contacts()

def search():
	global label_list
	db = sqlite3.connect('data.db')
	cursor = db.cursor()
	tele_list = []
	for q in cursor.execute("SELECT * FROM phonelist"):
		tele_list.append(q)
	
	if contact_was:
		for q in range(len(label_list)):
			label_list[q][0].destroy()
			label_list[q][1].destroy()
			label_list[q][2].destroy()

	label_list = []

	search = search_entry.get()
	for i in range(len(tele_list)):
		if search in tele_list[i][0]:
			name = Label(text = tele_list[i][0], bg = 'black', fg = 'white')
			number = Label(text = tele_list[i][1], bg = 'black', fg = 'white')
			delete_contact = Button(text = 'x', command = lambda: contact_delete(name))

			name.place(x = 10, y = 30 + i * 30, width = 100 ,height = 20)
			number.place(x = 120, y = 30 + i * 30, width = 100, height = 20)
			delete_contact.place(x = 225, y = 30 + i * 30, width = 20, height = 20)

			label_list.append((name, number, delete_contact))


root = Tk()
root.geometry("360x500")
root['bg'] = 'grey'

last_i = 0
contact_was = False
label_list = []

contacts()

root_name = Label(text = 'PhoneList', bg = 'grey', fg = 'white')
root_name.place(x = 0, y = 0, width = 250, height = 30)

plus_contact = Button(text='+', command = contact_add)
plus_contact.place(x = 225, y = 5, width = 20, height = 20)

search_button = Button(text = 'Search', command = search)
search_button.place(x = 10, y = 440, width = 230, height = 20)

search_entry = Entry()
search_entry.place(x = 10, y = 470, width = 230, height = 20)

root.mainloop()