import tkinter as tk
from tkinter import ttk
from BudgetFunctions import *
import User

# window = Tk()
LARGE_FONT = ("Verdana", 35)

class BudgetApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (loginPage, registerPage, budgetListPage):
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.geometry("600x600")
        self.show_frame(loginPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class loginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        name_label = ttk.Label(self, text="Name:", font = LARGE_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = LARGE_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        login_button = ttk.Button(self, text ="Login", command = lambda : [get_user(name_entry.get(), password_entry.get()), controller.show_frame(budgetListPage)])
        login_button.grid(row = 4, column = 2, padx = 10, pady = 10)
  
        register_button = ttk.Button(self, text ="Register", command = lambda : controller.show_frame(registerPage))
        register_button.grid(row = 4, column = 4, padx = 10, pady = 10)

class registerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        name_label = ttk.Label(self, text="Name:", font = LARGE_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = LARGE_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        register_button = ttk.Button(self, text ="Register", command = lambda : [create_new_user(), controller.show_frame(loginPage)])
        register_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text ="Back", command = lambda : controller.show_frame(loginPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)

class budgetListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Initialise treeview
        treeview = ttk.Treeview(self)
        treeview["columns"] = ("name", "budget", "final_week")  # Define the columns

        # Define column headings
        treeview.heading("#0", text = "Budget ID")
        treeview.heading("name", text = "Name")
        treeview.heading("budget", text = "Budget")
        treeview.heading("final_week", text = "Final Week")

        # Add sample data to the treeview
        treeview.insert("", "end", text="1", values=("John", "$100","Now"))
        treeview.insert("", "end", text="2", values=("$200", "kdf", "df"))
        treeview.insert("", "end", text="3", values=( "$300", "fkdf", "fk"))

        # Configure column widths
        treeview.column("name", width=100)
        treeview.column("budget", width=100)
        treeview.column("final_week", width=100)

        # Pack the Treeview widget
        treeview.pack(fill="both", expand=True)

        treeview.bind("<<TreeviewSelect>>", self.handle_selection)

        select_button = ttk.Button(self, text = "Select", command = self.run_budget)
        select_button.pack()

        back_button = ttk.Button(self, text = "Back", command = lambda: [self.back, controller.show_frame(loginPage)])
        back_button.pack()

    def handle_selection(self, event):
        selected_item = event.widget.selection()
        if selected_item:
            # Get the values of the selected item
            item_data = event.widget.item(selected_item)
            self.selected_item = {
                "text": item_data["text"],
                "values": item_data["values"]
            }

    def run_budget(self):
        if self.selected_item:
            # Use the selected item's values in your function
            budget_id = int(self.selected_item["text"])
            values = self.selected_item["values"]
            # Perform the desired action with the selected item's text and values
            print("Selected Item Text:", budget_id)
            print("Selected Item Values:", values)
    
    def back(self):
        current_user = None


class mainMenuPage:
    # global menu_frame 
    # def add_income_gui(self):
    #     menu_frame.destroy()
    #     add_income_frame.pack()
    #     current_budget = db.fetch("SELECT currentBudget FROM users WHERE username="+current_user)
    #     current_budget_label = Label(add_income_frame,font=("Ariel",12),text="Current budget: ")
    #     enter_label = Label(add_income_frame,font=("Ariel",12),text="Enter Income: ")
    #     enter_income_box = Entry(add_income_frame,width=70)
    #     confirm_button = Button(add_income_frame, text="Confirm Income",bg="white",width=20,height=3,command=db.execute("kd"))
    #     current_budget_label.grid(row=0,column=0)
    #     enter_label.grid(row=1,column=0)
    #     enter_income_box.grid(row=1,column=1)
    #     confirm_button.grid(row=2,column=1)
    
    # def enter_expenses_gui(self):
    #     menu_frame.destroy()
    #     enter_spend_frame.pack()
    #     current_budget = db.fetch("SELECT currentBudget FROM users WHERE username="+current_user)
    #     current_budget_label = Label(enter_spend_frame,font=("Ariel",12),text="Current budget: ")
    #     enter_label = Label(enter_spend_frame,font=("Ariel",12),text="Emter Expenses: ")
    #     enter_spend_box = Entry(enter_spend_frame,width=70)
    #     confirm_button = Button(enter_spend_frame, text="Confirm Expenses",bg="white",width=20,height=3,command=db.execute("kd"))
    #     current_budget_label.grid(row=0,column=0)
    #     enter_label.grid(row=1,column=0)
    #     enter_spend_box.grid(row=1,column=1)
    #     confirm_button.grid(row=2,column=1)

    # def change_week_gui(self):
    #     cd = changeData()
    #     menu_frame.destroy()
    #     change_week_frame.pack()
    #     current_week = db.fetch("SELECT currentWeek FROM users WHERE username="+current_user)
    #     current_week_label = Label(change_week_frame,font=("Ariel",12),text="Current Week: ")
    #     enter_label = Label(change_week_frame,font=("Ariel",12),text="Enter New Week: ")
    #     enter_week = Entry(change_week_frame,width=70)
    #     confirm_button = Button(change_week_frame, text="Confirm New Week",bg="white",width=20,height=3,command=lambda:cd.new_week(enter_week.getint))
    #     current_week_label.grid(row=0,column=0)
    #     enter_label.grid(row=1,column=0)
    #     enter_week.grid(row=1,column=1)
    #     confirm_button.grid(row=2,column=1)
        
    # def run(self):  
    #     menu_frame.pack()
    #     add_income_button = Button(menu_frame, text="Add Income",bg="white",width=20,height=3,command=self.add_income_gui)
    #     add_income_button.grid(row=6, column=5)
    #     enter_spend_button = Button(menu_frame, text="Enter Expenses",bg="white",width=20,height=3,command=self.enter_expenses_gui)
    #     enter_spend_button.grid(row=6, column=9)
    #     change_current_button = Button(menu_frame, text="Change Week",bg="white",width=20,height=3,command=self.change_week_gui)
    #     change_current_button.grid(row=6, column=13)
    pass


class budPage:
    global budget_frame
    global current_user

    def run(self):
        budgets = current_user.get_budgets()
        budget_frame.pack()

        
# def login_gui(name,password):
#     user_id = get_user(name,password)
#     if user_id == []:
#         print("Invalid Login")
        
#     else:
#         print("Valid Login")
#         # current_user = User(user_id)
#         # main = budgetGUI()
#         # main.run(user_id)
        

# def register_gui():
#     login_frame.destroy()
#     cd = changeData()
#     register_frame.pack()
#     name_label = Label(register_frame,font=("Ariel",12),text="Name: ")
#     name_box = Entry(register_frame,width=70)
#     pass_box = Entry(register_frame,width=70)
#     password_label = Label(register_frame,font=("Ariel",12),text="Password: ")
#     name_label.grid(row=2,column=1)
#     name_box.grid(row=2,column=2)
#     password_label.grid(row=3,column=1)
#     pass_box.grid(row=3,column=2)
#     confirm_button = Button(register_frame,text="Confirm",bg="white",width=20,height=3,command=lambda: cd.create_user(name_box.get(),pass_box.get()))
#     confirm_button.grid(row=4,column=2)

# def run_login_gui():
#     login_frame.pack()
#     name_label = Label(login_frame,font=("Ariel",12),text="Username: ")
#     name_box = Entry(login_frame,width=70)
#     pass_box = Entry(login_frame,width=70)
#     password_label = Label(login_frame,font=("Ariel",12),text="Password: ")
#     name_label.grid(row=2,column=1)
#     name_box.grid(row=2,column=2)
#     password_label.grid(row=3,column=1)
#     pass_box.grid(row=3,column=2)
#     login_button = Button(login_frame,text="Login",bg="white",width=20,height=3,command=lambda: login_gui(name_box.get(),pass_box.get()))
#     login_button.grid(row=4,column=2)
#     reg_button = Button(login_frame,text="Register",bg="white",width=20,height=3,command=register_gui)
#     reg_button.grid(row=6,column=1)

# window.title("Budget app")
# screen_height = window.winfo_screenheight()
# screen_width = window.winfo_screenwidth()
# window_size = (screen_height-(screen_height//10)) if screen_height < screen_width else (screen_width-(screen_width//10))
# window.geometry(str(window_size)+"x"+str(window_size))

# #App frames
# login_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# register_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# budget_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# menu_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# add_income_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# enter_spend_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")
# change_week_frame = Frame(window,bd=2,width=window_size,height=window_size,bg="grey")


current_user = None
# run_login_gui()

app = BudgetApp()
app.mainloop()