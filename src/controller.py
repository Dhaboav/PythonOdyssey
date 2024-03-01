from src.view import View
from src.model import Model
from random import randint


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__view = View(master=master, controller=self)

    # ============================ Password Generator ===========================
    def __save_timelog(self):
        with open(self.__model.get_password_path(), "w") as file:
            file.write(self.__model.get_timelog())

    def __save_data(self, data):
        with open(self.__model.get_password_path(), "a") as file:
            file.write("\n" + data)

    def __password_generator(self) -> list:
        __passwords = []
        for __category in self.__model.get_categories():
            __passwords.append(f'\n{__category}')
            for __month in self.__model.get_months():
                __number = randint(1000, 9999)
                __generated = f'{__month}_{__number}_{self.__model.get_year()}x_{__category}'
                __passwords.append(__generated)
        return __passwords
    # ===========================================================================

    # Handling event GUI
    def handle_menu_button(self, menu_id:str):
        __result = self.__model.get_menu(menu_id)
        if __result == "GenPassword":
            self.__save_timelog()
            __gen_pass = self.__password_generator()
            for __password in __gen_pass:
                self.__save_data(__password)

            self.__view.show_info_dialog('System Info', 'Done Generated Password')