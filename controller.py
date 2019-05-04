
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Controller:

    def __init__(self, files, listbox):
        self.files = files
        self.listbox = listbox

    def fileNotAlreadyAdded(self, v):
        for path in self.files:
            if v == path:
                return False
        return True

    def add(self):
        file_path = filedialog.askopenfilename()
        if file_path and self.fileNotAlreadyAdded(file_path):
            self.listbox.insert(len(self.files)+1, file_path)
            self.files.append(file_path)

    def remove(self):
        try:
            index = self.listbox.curselection()[0]
            del self.files[index]
            self.listbox.delete(self.listbox.curselection()[0])
        except IndexError:
            messagebox.showinfo("Error", "No files selected")

    def encrypt(self):
        if len(self.files)==0:
            messagebox.showinfo("Error", "No files has been selected for encryption")

        else:
            print("encrypt")

    def decrypt(self):
        if len(self.files)==0:
            messagebox.showinfo("Error", "No files has been selected for decryption")

        else:
            print("decrypt")
