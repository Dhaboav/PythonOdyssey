import tkinter as tk


class View:
    def __init__(self, master, controller) -> None:
        self.__controller = controller
        self.__component(master=master)

    def __component(self, master):
        pass