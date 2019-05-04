
import tkinter as tk

from controller import Controller
import ui

def main():
    # root window
    root = tk.Tk()
    root.title("Pycyptor")
    root.resizable(0, 0)
    root.geometry("500x300")
    top = tk.PanedWindow(root, bg="#303952")

    ctrl = Controller([], ui.setListbox(top))

    ui.setMenu(top, root, ctrl)
    ui.setButtons(top, root, ctrl)

    top.place(height=300, width=500, x=0, y=0)

    root.mainloop()


if __name__ == '__main__':
    main()
