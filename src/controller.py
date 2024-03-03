import os
from src.view import View
from random import randint
from src.model import Model
from src.custom_dialog import CustomDialog


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__master = master
        self.__view = View(master=self.__master, controller=self)

    # ============================ Password Generator ===========================
    def __save_timelog(self):
        with open(self.__model.get_password_path(), "w") as file:
            file.write(self.__model.get_timelog())

    def __save_data(self, data:str):
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
    # ============================ Change File Name =============================
    def __change_file(self, folder_path:str, name_format:str):
        __counter = 1
        for __filename in os.listdir(folder_path):
            __old_file_path = os.path.join(folder_path, __filename)
            if os.path.isfile(__old_file_path):
                _, __file_ext = os.path.splitext(__filename)
                __new_file_name = name_format.format(__counter)
                __new_file_path = os.path.join(folder_path, __new_file_name + __file_ext)
                os.rename(__old_file_path, __new_file_path)
                __counter += 1
        self.__view.show_info_dialog('System Info', f'Done changed name of {__counter - 1} files')
    # ===========================================================================

    # Handling event GUI
    def handle_menu_button(self, menu_id:str):
        __result = self.__model.get_menu(menu_id)
        if __result == 'GenPassword':
            self.__save_timelog()
            __gen_pass = self.__password_generator()
            for __password in __gen_pass:
                self.__save_data(__password)

            self.__view.show_info_dialog('System Info', 'Done Generated Password')

        elif __result == 'ChangeFileName':
            __change = CustomDialog(root=self.__master)
            __feedback = __change.result
            if __feedback:
                __folder_path, __name = __feedback
                self.__change_file(folder_path=__folder_path, name_format=__name + '{}')