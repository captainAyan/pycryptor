
import os
from tkinter import filedialog
from tkinter import messagebox

import utility as util
from cryptography import Cryptography as crypt


class Controller:

    def __init__(self, files, listbox):
        self.files = files
        self.listbox = listbox

    # adds file to list
    def add(self):

        file_path = filedialog.askopenfilename()
        if file_path and util.filenotalreadyadded(file_path, self.files):

            self.listbox.insert(len(self.files)+1, file_path)
            self.files.append(file_path)

    # removes file from list
    def remove(self):

        try:

            index = self.listbox.curselection()[0]
            del self.files[index]
            self.listbox.delete(self.listbox.curselection()[0])
        except IndexError:
            messagebox.showerror("Error", "No files selected")

    # starts encryption process
    def encrypt(self, password):

        if len(self.files) == 0:
            messagebox.showerror("Error", "No files has been selected for encryption")

        elif len(password) == 0:
            messagebox.showerror("Error", "No passwords entered for encryption")

        else:
            for file_path in self.files:

                try:

                    dir_path = util.getdirectorypathfromfilepath(file_path)
                    f_name = util.getfilenamefromfilepath(file_path)

                    if not util.getfileextensionfromfilename(f_name) == "enc":
                        f_readable_data = open(file_path, "r").read()
                        f_enc = open(dir_path + f_name + ".enc", "w")
                        f_enc.write(crypt.encrypt(f_readable_data, password))
                        f_enc.close()

                    else:
                        messagebox.showwarning("Wrong file", "'.enc' files cannot be encrypted")
                        return

                except :
                    messagebox.showerror("Error", "Error occurred")
                    return

            messagebox.showinfo("Encrypted", "Files encrypted and save on the folder")

    # starts decryption process
    def decrypt(self):

        if len(self.files) == 0:
            messagebox.showerror("Error", "No files has been selected for decryption")

        else:
            print("decrypt")
