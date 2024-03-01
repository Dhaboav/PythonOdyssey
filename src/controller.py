from view import View
from model import Model

class Controller:
    def __init__(self, master) -> None:
        self._model = Model()
        self._view = View(master=master, controller=self)