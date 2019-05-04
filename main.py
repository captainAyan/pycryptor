
import tkinter as tk
import tkinter.font as tkFont

from controller import Controller


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        top = tk.PanedWindow(root, bg="#303952")
        custom_font = tkFont.Font(size=10)

        # setup list
        ctrl = Controller([], tk.Listbox(top, borderwidth=0, highlightbackground="#596275", bg="#596275", fg="#ffffff"))
        tk.Listbox(top, borderwidth=0, highlightbackground="#596275", bg="#596275", fg="#ffffff")

        # input box
        password_label = tk.Label(top, bg="#303952", fg="#ffffff", text="Password :")
        password_input = tk.Entry(top, borderwidth=0, highlightbackground="#596275", bg="#596275", fg="#ffffff",
                            font=custom_font)

        # top menu
        menubar = tk.Menu(top)
        filemenu1 = tk.Menu(menubar, tearoff=0)
        filemenu1.add_command(label="Add", command=ctrl.add)
        filemenu1.add_command(label="Encrypt", command=lambda: ctrl.encrypt(password_input.get()))
        filemenu1.add_command(label="Decrypt", command=ctrl.decrypt)
        filemenu1.add_separator()
        filemenu1.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Options", menu=filemenu1)
        filemenu2 = tk.Menu(menubar, tearoff=0)
        filemenu2.add_command(label="Help")
        filemenu2.add_separator()
        filemenu2.add_command(label="About")
        menubar.add_cascade(label="Help", menu=filemenu2)

        # encryption and decryption button
        encrypt_btn = tk.Button(top, text="Encrypt", command=lambda: ctrl.encrypt(password_input.get()), bg="#596275",
                                fg="#ffffff", borderwidth=0, font=custom_font)
        decrypt_btn = tk.Button(top, text="Decrypt", command=ctrl.decrypt, bg="#596275", fg="#ffffff", borderwidth=0,
                                font=custom_font)

        # file add and remove button
        add_btn = tk.Button(top, text="Add", command=ctrl.add, bg="#546de5", fg="#ffffff", borderwidth=0)
        remove_btn = tk.Button(top, text="Remove", command=ctrl.remove, bg="#e15f41", fg="#ffffff", borderwidth=0)

        # element placement
        add_btn.place(height=30, width=60, x=350, y=260)
        remove_btn.place(height=30, width=70, x=420, y=260)
        encrypt_btn.place(height=40, width=100, x=10, y=10)
        decrypt_btn.place(height=40, width=100, x=10, y=60)
        ctrl.listbox.place(height=210, width=370, x=120, y=10)
        password_label.place(height=20, width=60, x=120, y=230)
        password_input.place(height=20, width=300, x=190, y=230)
        top.place(height=300, width=500, x=0, y=0)
        root.config(menu=menubar)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pycyptor")
    root.resizable(0, 0)
    root.geometry("500x300")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
