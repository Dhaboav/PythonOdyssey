import json
from datetime import datetime as time


class Model:
    def __init__(self):
        with open('config.json', 'r') as json_file:
            __data = json.load(json_file)

        self.__password_path = __data['filePath']
        self.__categories = [
            __data['categories']['1'], __data['categories']['2'],
            __data['categories']['3']
        ]
        
        self.__date = time.now()
        self.__months = [
            __data['months']['1'], __data['months']['2'], __data['months']['3'],
            __data['months']['4'], __data['months']['5'], __data['months']['6'],
            __data['months']['7'], __data['months']['8'], __data['months']['9'],
            __data['months']['10'], __data['months']['11'], __data['months']['12']
        ]

        self.__menu = __data['menu']

    # Getter
    def get_password_path(self) -> str:
        return self.__password_path
    
    def get_categories(self) -> list:
        return self.__categories
    
    def get_year(self) -> int:
        return self.__date.year
    
    def get_months(self) -> list:
        return self.__months
    
    def get_timelog(self) -> str:
        return f'{self.__date:%Y-%m-%d}, {self.__date:%I:%M %p}'
    
    def get_menu(self, menu_id) -> str:
        return self.__menu.get(menu_id, None)