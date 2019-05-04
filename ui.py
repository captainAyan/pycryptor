
import tkinter as tk
import tkinter.font as tkFont


def setMenu(top, root, ctrl): 
	# top menu
	menubar = tk.Menu(top)
	filemenu1 = tk.Menu(menubar, tearoff=0)
	filemenu1.add_command(label="Add", command=ctrl.add)
	filemenu1.add_command(label="Encrypt", command=ctrl.encrypt)
	filemenu1.add_command(label="Decrypt", command=ctrl.decrypt)
	filemenu1.add_separator()
	filemenu1.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="Options", menu=filemenu1)
	filemenu2 = tk.Menu(menubar, tearoff=0)
	filemenu2.add_command(label="Help")
	filemenu2.add_separator()
	filemenu2.add_command(label="About")
	menubar.add_cascade(label="Help", menu=filemenu2)

	root.config(menu=menubar)


def setButtons(top, root, ctrl): 
	custom_font = tkFont.Font(size=10)
	add_btn = tk.Button(top, text="Add", command=ctrl.add, bg="#546de5", fg="#ffffff", borderwidth=0)
	remove_btn = tk.Button(top, text="Remove", command=ctrl.remove, bg="#e15f41", fg="#ffffff", borderwidth=0) 
	encrypt_btn = tk.Button(top, text="Encrypt", command=ctrl.encrypt, bg="#596275", fg="#ffffff", borderwidth=0, font=custom_font)
	decrypt_btn = tk.Button(top, text="Decrypt", command=ctrl.decrypt, bg="#596275", fg="#ffffff", borderwidth=0, font=custom_font)
	add_btn.place(height=30, width=60, x=350, y=260)
	remove_btn.place(height=30, width=70, x=420, y=260)
	encrypt_btn.place(height=40, width=100, x=10, y=10)
	decrypt_btn.place(height=40, width=100, x=10, y=60)
	ctrl.listbox.place(height=240, width=370, x=120, y=10)

def setListbox(top):
	return tk.Listbox(top, borderwidth=0, highlightbackground="#596275", bg="#596275", fg="#ffffff")