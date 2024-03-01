import json
from datetime import datetime as time


class Model:
    def __init__(self):
        with open('config.json', 'r') as json_file:
            __data = json.load(json_file)

        self.password_path = __data['filePath']
        self.categories = [
            __data['categories']['1'], __data['categories']['2'],
            __data['categories']['3']
        ]
        
        self.date = time.now()
        self.months = [
            __data['months']['1'], __data['months']['2'], __data['months']['3'],
            __data['months']['4'], __data['months']['5'], __data['months']['6'],
            __data['months']['7'], __data['months']['8'], __data['months']['9'],
            __data['months']['10'], __data['months']['11'], __data['months']['12']
        ]

    # Getter
    def get_password_path(self):
        return self.password_path
    
    def get_categories(self):
        return self.categories
    
    def get_year(self):
        return self.date.year
    
    def get_months(self):
        return self.months
    
    def get_timelog(self):
        return f'{self.date:%Y-%m-%d}, {self.date:%I:%M %p}'