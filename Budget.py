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

def add_income(): #will add user's income to their total budget
    pass

def enter_spend(): #will take user to screen to input their spending
    pass

def change_week(): #will allow user to change current week
    pass

def change_num_of_weeks_budget(): #choose how many weeks you need to budget for
    pass

def view_budget(budget,currentWeek):
    pass

def is_valid_login(name,hash_pass):
    db = DatabaseConnection()
    user = db.fetch("SELECT * FROM users WHERE username="+name+" AND password=hash_pass")
    if user != None:
        return True
    else: 
        return False
    

def authenticate_login(name,password):
    hash_pass = hash(password)
    if is_valid_login(name,hash_pass):
        return True
    else:
        return False