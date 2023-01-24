import tkinter as tk

def check_key(key:str,against:list):
	count=0
	for k in against:
		if k==key or k==key+str(count):
			count+=1
			print('check key:',k,' found:',count)
	if count>0:
		key=key+str(count)
	return key

def check_name(name:str,against:list,dash=''):
	count=0
	for n in against:
		if n==name or n==name+dash+str(count):
			count+=1
	if count>0:
		name=name+dash+str(count)
	return name

def step_grid(context):
	context.curColumn+=1
	if context.curColumn>context.maxColumn:
		context.curRow+=1

class Menu(tk.Menu):
	def __init__(self,container,**kwargs):
		super().__init__(container,**kwargs)
		self.title='menu'
		if 'title' in kwargs:self.title=kwargs['title']
		self.items=[]
		self.itemCount=0

	def add_items(self,items:list)->int:
	#items=[{'t':type,'l':label,'c':command,'m':submenu},{'t':type,'l':label,'c':command,'m':submenu}]
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

def add_panel(self,panel,key='',style='normal'):
	key=check_key(key,self.objects)

	if self.gridtype==-1:self.gridtype=0

	if self.gridtype==0:
		fill='none'
		expand=False
		if style=='normal':
			fill='none'
			expand=False
		if style=='full':
			fill='both'
			expand=True
		if style=='horizontal':
			fill='x'
			expand=True
		if style=='vertical':
			fill='y'
			expand=True
		panel.base.pack(fill=fill,expand=expand,padx=2,pady=2)
		print('packed:',panel,' to window')
	if self.gridtype==1:
		anchor='nw'
		sticky='nw'
		if style=='normal':
			anchor='nw'
			sticky='nw'
		if style=='full':
			anchor='nw'
			sticky='nsew'
		if style=='horizontal':
			anchor='nw'
			sticky='nsew'
		if style=='vertical':
			anchor='nw'
			sticky='nsew'
		panel.base.grid(row=self.curRow,column=self.curColumn,anchor='nw',sticky='nsew',padx=2,pady=2)
		step_grid(self)
	self.objects[key]=panel
	return key,panel