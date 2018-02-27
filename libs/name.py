import json
API = None


class SAPI:
    def __init__(self, api):
        global API
        API = api


class Name:
    DB = {}

    def __init__(self):
        with open('dlcs/default/db/names.json', 'r') as dbfile:
            self.DB = json.loads(dbfile.read())

    def get_new_name(self, gender, length):
        name = ''
        if gender == 'male':
            pass
        if gender == 'female':
            pass
        if length == 3:
            if gender == 'male':
                pass
            if gender == 'female':
                pass
        return
