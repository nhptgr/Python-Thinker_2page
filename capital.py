#!/usr/bin/env python2
import os; from tkinter import *
# classes + instances
class Capit():
	def __init__(self, country, image):
		self.country=country
		self.image=image
rome=Capit('Italy','capital-rom.gif');paris=Capit('France','capital-par.gif');oslo=Capit('Norway','capital-osl.gif')
# functions (d_path pyinstaller add-data path)
def d_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)
def update(*args):
	getvar = entvar.get()
	if getvar not in ["rome","paris","oslo"]:
		entvar.set(""); lblvar.set(""); return
	cityvar = eval(getvar, {'__builtins__': None},{"rome": rome, "paris": paris, "oslo": oslo})
	lblvar.set(cityvar.country);cityph=PhotoImage(file=(d_path(cityvar.image)));lb2.image=cityph;lb2.configure(image=cityph)
	return
# main window centered + menus
win=Tk(); win.title('CITY'); x_pos=(win.winfo_screenwidth()/2-180); y_pos=(win.winfo_screenheight()/2-60); win.geometry("360x120+%d+%d"%(x_pos,y_pos)); win.minsize(360,120)
win.grid_columnconfigure(0, weight=1); win.grid_columnconfigure(1, weight=1); win.grid_rowconfigure(0,weight=1)
mnu=Menu(win); win.config(menu=mnu); mn1=Menu(mnu); mnu.add_cascade(label='Menu',menu=mn1); mn1.add_separator(); mn1.add_command(label="Exit",command=win.quit)
# frames (only minsize required)
lft=Frame(win,bg="white"); lft.grid(row=0,column=0,padx=10,pady=10)
lft.grid_rowconfigure(0,minsize=50);lft.grid_rowconfigure(1,minsize=50)
lft.grid_columnconfigure(0,minsize=115);lft.grid_columnconfigure(1,minsize=115)
rgt=Frame(win,bg="black"); rgt.grid(row=0,column=1,padx=(0,10),pady=10)
rgt.grid_rowconfigure(0,minsize=100)
rgt.grid_columnconfigure(0,minsize=100)
# widgets
entvar=StringVar(); ent=Entry(lft, textvariable=entvar, width=10); ent.bind("<Return>", update)
lblvar=StringVar(); lb1=Label(lft,textvariable=lblvar, bg="white")
bot=Button(lft,text="Quit",width=10,command=win.quit)
cityph=PhotoImage(file=(d_path(rome.image))); lb2=Label(rgt, image=cityph)
ent.grid(row=0,column=0,sticky=E, padx=5)
lb1.grid(row=0,column=1,sticky=W, padx=5)
bot.grid(row=1,columnspan=2)
lb2.grid(row=0,column=0,sticky=NSEW)
win.mainloop()