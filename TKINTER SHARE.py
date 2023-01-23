import tkinter as tk

class Menu(tk.Menu):
	def __init__(self,container,**kwargs):
		super().__init__(container,**kwargs)
		self.title='menu'
		if 'title' in kwargs:self.title=kwargs['title']
		self.items=[]
		self.itemCount=0

	def add_items(self,items:list)->int:
	#items=[{'t':type,'l':label,'c':command,'m':menu}]
		for item in items:
			if item['t']=='separator' or item['t']=='s':
				self.add_separator()
			if item['t']=='check':
				self.add_checkbutton()
			if item['t']=='radio':
				self.add_radiobutton()
			if item['t']=='item':
				self.add_command()
			if item['t']=='sub':
				if 'l' in item:
					self.add_cascade(menu=item['m'],label=item['l'])
				if 'l' not in item:
					self.add_cascade(menu=item['m'],label='-Menu')
			#---
			if item['t']!='sub':
				if 'l' in item:
					self.entryconfig(self.itemCount,label=item['l'])
			if 'onVal' in item:
				self.entryconfig(self.itemCount,onvalue=item['onVal'])
			if 'offVal' in item:
				self.entryconfig(self.itemCount,offvalue=item['offVal'])
			if 'v' in items:
				self.entryconfig(self.itemCount,variable=item['v'])
			if 'c' in item:
				self.entryconfig(self.itemCount,command=item['c'])
			if 'col' in item:
				self.entryconfig(self.itemCount,selectcolor=item['col'])
			if 'acel' in item:
				self.entryconfig(self.itemCount,accelerator=item['acel'])
		self.itemCount+=1#|Needs to be inside loop, to iterate
		print('Added items',self.itemCount,' to menu')