import tkinter as tk
from tkinter import messagebox


class View:
    def __init__(self, master, controller):
        self.__controller = controller
        self.__component(master=master)

    def __component(self, master):
        __menu_frame = tk.LabelFrame(master=master, text='MENU')
        __pass_button = tk.Button(
            master=__menu_frame, text='Password Generator', width=20, 
            foreground='white', background='blue', 
            command=lambda: self.__controller.handle_menu_button(menu_id='1')
        )

        __menu_frame.pack()
        __pass_button.pack()

    def show_info_dialog(self, title:str, message:str):
        messagebox.showinfo(title, message)