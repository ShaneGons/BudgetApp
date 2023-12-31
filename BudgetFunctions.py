from tkinter import *
from datatabase import *
import hashlib

currentWeek: int
db = DatabaseConnection()

def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')
    
    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    return password_hash

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

#Gets the user's ID from the database using their login credentials
def get_user(name,password):
    hash_pass = hash_password(password)
    password = None
    sql = "SELECT user_id FROM tbl_users WHERE name=? AND password=?"
    values = (name, hash_pass)
    user_id = db.fetch_conditions(sql,values)
    try:
        return user_id[0][0]
    except:
        raise Exception("Invalid login credentials")

#Adds new user to database
def create_new_user(name, password):
    hash_pass = hash_password(password)
    password = None
    sql = "INSERT INTO tbl_users (name, password) VALUES (?, ?)"
    values = (name, hash_pass)
    if db.execute(sql, values):
        print("User sucessfully created")
    else:
        print("Failed to create user")

def change_weeks():
    pass

    