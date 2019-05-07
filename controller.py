
from tkinter import filedialog
from tkinter import messagebox

import utility as util
from cryptography import Cryptography as crypt


class Controller:

    def __init__(self, files, listbox):
        self.files = files
        self.listbox = listbox
        self.error = ""

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
            return

        elif len(password) == 0:
            messagebox.showerror("Error", "No passwords entered for encryption")
            return

        else:
            for i, file_path in enumerate(self.files):
                try:
                    dir_path = util.getdirectorypathfromfilepath(file_path)
                    f_name = util.getfilenamefromfilepath(file_path)

                    if not util.getfileextensionfromfilename(f_name) == "enc":

                        try:
                            f_readable_data = open(file_path, "rb").read()
                        except FileNotFoundError as e:
                            self.error += ("Error on file '" + file_path + "'. Not found during encryption. \n")
                            self.listbox.itemconfig(i, {"bg": util.color_danger})

                        else:
                            f_enc = open(dir_path + f_name + ".enc", "wb")
                            f_enc.write(crypt.encrypt(f_readable_data, password))
                            f_enc.close()
                            self.listbox.itemconfig(i, {"bg": util.color_success})

                    else:
                        self.error += ("Error on file '" + file_path + "'. '.enc' files cannot be encrypted. \n")
                        self.listbox.itemconfig(i, {"bg": util.color_danger})

                except Exception as e:
                    self.error += ("Error on file '" + file_path + "'. "+e+". \n")

        messagebox.showinfo("Encrypted", "Process ended! Files encrypted and save on the folder. \n" + self.error)
        self.error = ""

    # starts decryption process
    def decrypt(self, password):

        if len(self.files) == 0:
            messagebox.showerror("Error", "No files has been selected for decryption")

        else:
            print("decrypt")
