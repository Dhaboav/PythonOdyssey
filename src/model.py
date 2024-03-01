import json


class Model:
    def __init__(self):
        with open('config.json', 'r') as json_file:
            data = json.load(json_file)