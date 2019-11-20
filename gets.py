import json
from tkinter import *

#Retrieves the username of the user that is currently logged in
def getRecent():
    with open('users.json') as json_file:
        data = json.load(json_file)
        return data["recent"]

def getValue(user, key):
    with open('users.json') as json_file:
        data = json.load(json_file)
        return data[user][key]
