from tkinter import *
from datatabase import *

currentWeek: int

def loadProgram(): #loads all the required data needed, such as current week
    tuple = read_from_database() #database return tuple that contains current week and budget left
    currentWeek = tuple[0]
    budget = tuple[1]
    weekSpend = tuple[2]
    weekIncome = tuple[3]
    #the advantange of having variables instead of writing to the database is that the user can make
    #changes and then discard them if they want to, database acts as a save state

def read_from_database():
    pass


def view_budget(budget, currentWeek):
    pass

def get_user(name,password):
    hash_pass = hash(password)
    db = DatabaseConnection()
    user = db.fetch("SELECT user_id FROM tbl_users WHERE f_name="+name+" AND password="+hash_pass+";")
    return user