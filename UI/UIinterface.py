#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import csv
import pprint
from tkinter import Tk, BOTH
from tkinter.ttk import Frame

f = open('../newresult.csv')
result = csv.reader(f)
filedic = {}
filepdic = {}
for row in result:
	if filedic.get(row[4]):
		filedic[row[4]] += 1
		if (row[3] == 'positive'):
			filepdic[row[4]] += 1
	else:
		filedic[row[4]] = 1
		if (row[3] == 'positive'):
			filepdic[row[4]] = 1
		else:
			filepdic[row[4]] = 0
f.close()
#pprint.pprint(filepdic)
#pprint.pprint(filedic)


root = tk.Tk()
root.title("movie")
root.geometry("800x600")

titile = tk.Label(root, text = 'Which film are you looking for?', font = 'Helvetica 30 bold', fg = 'blue')
titile.place(x = 400, y = 200, anchor = "center")
entry = tk.Entry(root, bd = 5, width = 50)
entry.place(x = 400, y = 400, anchor = "center")

def judge():
	re1 = entry.get()
	re = re1.lower()
	root1 = tk.Toplevel(root)
	titlestrl = ["Search Result for", re1]
	titlestr = ' '.join(titlestrl)
	root1.title(titlestr)
	root1.geometry("600x400+100+100")
	if filedic.get(re):
		percent = filepdic[re]/filedic[re]
		print(percent)
		if (percent > 0.5):
			ptextl = ["It is a good movie!\n ", str(round(percent*100, 2)), "% of ", str(filedic[re]), " audiences love it!"]
			ptext = ''.join(ptextl)
			print(ptext)
			pjudge = tk.Label(root1, text = ptext, font = 'Helvetica 30 bold', fg = 'blue')
			pjudge.place(x = 300, y = 200, anchor = "center")
		else:
			ntextl = ["It is a bad movie!\n Only ",str(round(percent*100, 2)),"% of ", str(filedic[re]), " audiences love it..."]
			ntext = ''.join(ntextl)
			print(ntext)
			njudge = tk.Label(root1, text = ntext, font = 'Helvetica 30 bold', fg = 'red')
			njudge.place(x = 300, y = 200, anchor = "center")
	else:
		nonetext = "We are sorry. We can't find the movie."
		print(nonetext)
		nonejudge = tk.Label(root1, text = "We are sorry. We can't find the movie.", font = 'Helvetica 30 bold', fg = "grey")
		nonejudge.place(x = 300, y = 200, anchor = "center")
	entry.delete(0,20)
	print(entry.get())


b = tk.Button(root, text = "Search", width = 50, command = judge)
b.place(x = 400, y = 500, anchor = "center")

root.mainloop()
