import tkinter as tk
from src.controller import Controller


if __name__ == '__main__':
    root = tk.Tk()
    root.title('GUI')
    root.resizable(width=False, height=False)
    run = Controller(master=root)
    root.mainloop()