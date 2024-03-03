import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import messagebox, filedialog


class CustomDialog(simpledialog.Dialog):
    def __init__(self, root):
        self.custom_root = root
        super().__init__(self.custom_root)

    def body(self, master):
        tk.Label(master, text="Enter a name:").grid(row=0, sticky=tk.W)
        tk.Label(master, text="Select a folder:").grid(row=1, sticky=tk.W)

        self.__entry_name = tk.Entry(master)
        self.__entry_name.grid(row=0, column=1)

        self.__entry_path = tk.Entry(master)
        self.__entry_path.grid(row=1, column=1)

        self.__button_browse = tk.Button(master, text="Browse", command=self.__select_folder)
        self.__button_browse.grid(row=1, column=2, padx=5)

    def __select_folder(self):
        folder_path = filedialog.askdirectory(title="Select a Folder")
        if folder_path:
            self.__entry_path.delete(0, tk.END)
            self.__entry_path.insert(tk.END, folder_path)

    def apply(self):
        __name = self.__entry_name.get()
        __folder_path = self.__entry_path.get()

        if not __name:
            self.__show_error_dialog("Error", "Please enter a name")
            return

        if not __folder_path:
            self.__show_error_dialog("Error", "Please select a folder")
            return

        self.result = (__folder_path, __name)
    
    def __show_error_dialog(self, title:str, message:str):
        messagebox.showerror(title, message)