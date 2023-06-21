from sqlite3 import Row
import tkinter as tk
from tkinter import *
from BudgetFunctions import *
import User

window = Tk()

class mainMenuGUI:
    global menu_frame 
    def add_income_gui(self):
        menu_frame.destroy()
        add_income_frame.pack()
        current_budget = db.fetch("SELECT currentBudget FROM users WHERE username="+current_user)
        current_budget_label = Label(add_income_frame,font=("Ariel",12),text="Current budget: ")
        enter_label = Label(add_income_frame,font=("Ariel",12),text="Enter Income: ")
        enter_income_box = Entry(add_income_frame,width=70)
        confirm_button = Button(add_income_frame, text="Confirm Income",bg="white",width=20,height=3,command=db.execute("kd"))
        current_budget_label.grid(row=0,column=0)
        enter_label.grid(row=1,column=0)
        enter_income_box.grid(row=1,column=1)
        confirm_button.grid(row=2,column=1)
    
    def enter_expenses_gui(self):
        menu_frame.destroy()
        enter_spend_frame.pack()
        current_budget = db.fetch("SELECT currentBudget FROM users WHERE username="+current_user)
        current_budget_label = Label(enter_spend_frame,font=("Ariel",12),text="Current budget: ")
        enter_label = Label(enter_spend_frame,font=("Ariel",12),text="Emter Expenses: ")
        enter_spend_box = Entry(enter_spend_frame,width=70)
        confirm_button = Button(enter_spend_frame, text="Confirm Expenses",bg="white",width=20,height=3,command=db.execute("kd"))
        current_budget_label.grid(row=0,column=0)
        enter_label.grid(row=1,column=0)
        enter_spend_box.grid(row=1,column=1)
        confirm_button.grid(row=2,column=1)

    def change_week_gui(self):
        cd = ChangeData()
        menu_frame.destroy()
        change_week_frame.pack()
        current_week = db.fetch("SELECT currentWeek FROM users WHERE username="+current_user)
        current_week_label = Label(change_week_frame,font=("Ariel",12),text="Current Week: ")
        enter_label = Label(change_week_frame,font=("Ariel",12),text="Enter New Week: ")
        enter_week = Entry(change_week_frame,width=70)
        confirm_button = Button(change_week_frame, text="Confirm New Week",bg="white",width=20,height=3,command=lambda:cd.new_week(enter_week.getint))
        current_week_label.grid(row=0,column=0)
        enter_label.grid(row=1,column=0)
        enter_week.grid(row=1,column=1)
        confirm_button.grid(row=2,column=1)
        
    def run(self):  
        menu_frame.pack()
        add_income_button = Button(menu_frame, text="Add Income",bg="white",width=20,height=3,command=self.add_income_gui)
        add_income_button.grid(row=6, column=5)
        enter_spend_button = Button(menu_frame, text="Enter Expenses",bg="white",width=20,height=3,command=self.enter_expenses_gui)
        enter_spend_button.grid(row=6, column=9)
        change_current_button = Button(menu_frame, text="Change Week",bg="white",width=20,height=3,command=self.change_week_gui)
        change_current_button.grid(row=6, column=13)

class ChangeData:
    def new_week(budget, new_week):
        if budget.change_week(new_week):
            pass
        else:
            return False
        

class budgetGUI:
    global budget_frame
    global current_user

    def run(self):
        budgets = current_user.get_budgets()
        budget_frame.pack()
        
        
 

def login_gui(name,password):
    user_id = get_user(name,password)
    if user_id == None:
        print("Invalid Login")
        login_frame.destroy()
        main = budgetGUI()
        main.run(user_id)
    else:
        current_user = User(user_id)
        print("Valid Login")

def register_gui():
    print("Register")


window.title("Budget app")
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
window_size = (screen_height-(screen_height//10)) if screen_height < screen_width else (screen_width-(screen_width//10))
window.geometry(str(window_size)+"x"+str(window_size))

#App frames
login_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
budget_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
menu_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
add_income_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
enter_spend_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
change_week_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
current_user : User()


db = DatabaseConnection()
db.createDatabase()
current_user = ""
login_frame.pack()
name_label = Label(login_frame,font=("Ariel",12),text="Username: ")
name_box = Entry(login_frame,width=70)
pass_box = Entry(login_frame,width=70)
password_label = Label(login_frame,font=("Ariel",12),text="Password: ")
name_label.grid(row=2,column=1)
name_box.grid(row=2,column=2)
password_label.grid(row=3,column=1)
pass_box.grid(row=3,column=2)
login_button = Button(login_frame,text="Login",bg="white",width=20,height=3,command=lambda: login_gui(name_box.get(),pass_box.get()))
login_button.grid(row=4,column=2)
reg_button = Button(login_frame,text="Register",bg="white",width=20,height=3,command=register_gui())
reg_button.grid(row=6,column=1)

window.mainloop()