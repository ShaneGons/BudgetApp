import tkinter as tk
from tkinter import ttk
from BudgetFunctions import *
from User import *
from Budget import *
from tkcalendar import Calendar
from datetime import date

# window = Tk()
MEDIUM_FONT = ("Verdana", 15)
current_user = User()
current_budget = Budget()

class BudgetApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (loginPage, registerPage, budgetListPage, createBudgetPage, mainMenuPage, incomePage, expensePage, changeWeeksPage, changeBudgetWeeks):
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
        
        name_label = ttk.Label(self, text= "Name:", font = MEDIUM_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = MEDIUM_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        login_button = ttk.Button(self, text = "Login", command = lambda : [login(name_entry.get(), password_entry.get()), clear_entry(name_entry), 
                                                                            clear_entry(password_entry), budgetListPage.load(), controller.show_frame(budgetListPage)])
        login_button.grid(row = 4, column = 2, padx = 10, pady = 10)
  
        register_button = ttk.Button(self, text = "Register", command = lambda : [clear_entry(name_entry), clear_entry(password_entry), controller.show_frame(registerPage)])
        register_button.grid(row = 4, column = 4, padx = 10, pady = 10)

def login(name, password):
    user_id = get_user(name, password)
    password = None
    if user_id != None:
        current_user.set_user_id(user_id)
    


class registerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        name_label = ttk.Label(self, text= "Name:", font = MEDIUM_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = MEDIUM_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        register_button = ttk.Button(self, text = "Register", command = lambda : [create_new_user(name_entry.get(),password_entry.get()), 
                                                                                  clear_entry(name_entry), clear_entry(password_entry), controller.show_frame(loginPage)])
        register_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(loginPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)

class budgetListPage(tk.Frame):
    def __init__(self, parent, controller):
        budget_list = current_user.get_budgets()
        tk.Frame.__init__(self, parent)
        
        #Initialise treeview table
        global budget_table
        budget_table = ttk.Treeview(self)
        budget_table["columns"] = ("name", "budget", "num_weeks")  # Define the columns

        # Define column headings
        budget_table.heading("#0", text = "Budget ID")
        budget_table.heading("name", text = "Name")
        budget_table.heading("budget", text = "Budget")
        budget_table.heading("num_weeks", text = "Remaining Weeks")

        # Add sample data to the budget_table

        # Configure column widths
        budget_table.column("name", width=100)
        budget_table.column("budget", width=100)
        budget_table.column("num_weeks", width=100)

        # Pack the Treeview widget
        budget_table.pack(fill="both", expand=True)

        budget_table.bind("<<TreeviewSelect>>", self.handle_selection)

        select_button = ttk.Button(self, text = "Select", command = lambda : [self.run_budget(), mainMenuPage.load(), controller.show_frame(mainMenuPage)])
        select_button.pack()

        create_budget_button = ttk.Button(self, text = "Create New Budget", command = lambda : controller.show_frame(createBudgetPage))
        create_budget_button.pack()

        back_button = ttk.Button(self, text = "Back", command = lambda: [self.back(), controller.show_frame(loginPage)])
        back_button.pack()
    
    def load():
        def clear_table():
            for budget in budget_table.get_children():
                budget_table.delete(budget)
                
        clear_table()
        budget_list = current_user.get_budgets()
        for i in range(len(budget_list)):
            budget_str = "{:.2f}".format(budget_list[i][2])
            budget_table.insert("", "end", text=str(budget_list[i][0]), values=(budget_list[i][1],budget_str,budget_list[i][3]))
        
        

    def handle_selection(self, event):
        selected_item = event.widget.selection()
        if selected_item:
            # Get the values of the selected item
            item_data = event.widget.item(selected_item)
            self.selected_item = {
                "budget_id": item_data["text"],
                "values": item_data["values"]
            }

    def run_budget(self):
        if self.selected_item:
            # Use the selected item's values in your function
            budget_id = int(self.selected_item["budget_id"])
            values = self.selected_item["values"]
            # Perform the desired action with the selected item's text and values
            current_budget.set_budget_id(budget_id)
            current_budget.set_budget(float(values[1]))
            current_budget.set_num_weeks(int(values[2]))
    
    def back(self):
        current_user.set_user_id(-1)


class createBudgetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        name_label = ttk.Label(self, text= "Budget Name:", font = MEDIUM_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        budget_label = ttk.Label(self, text = "Budget:", font = MEDIUM_FONT)
        budget_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        budget_entry = ttk.Entry(self, text = "Budget")
        budget_entry.grid(row = 1, column = 2, padx = 15, pady = 10)

        num_weeks_label = ttk.Label(self, text = "No. of Weeks:", font = MEDIUM_FONT)
        num_weeks_label.grid(row = 2, column = 1, padx = 10, pady = 10)

        num_weeks_entry = ttk.Entry(self, text = "Weeks")
        num_weeks_entry.grid(row = 2, column = 2, padx = 15, pady = 10)
  
        create_button = ttk.Button(self, text = "Create", command = lambda : [current_user.add_budget(name_entry.get(),budget_entry.get(), num_weeks_entry.get()), 
                                                                              clear_entry(name_entry), clear_entry(budget_entry), clear_entry(num_weeks_entry), 
                                                                              budgetListPage.clear_table(), budgetListPage.load(), controller.show_frame(budgetListPage)])
        create_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(budgetListPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class mainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global week_label
        global total_budget_label
        global weekly_budget_label
        
        week_label = ttk.Label(self, text= "Weeks Remaining: "+str(current_budget.num_weeks), font = MEDIUM_FONT)
        week_label.grid(row = 0, column = 1, padx = 10, pady = 10)

        total_budget_label = ttk.Label(self, text = "Remaining Budget: "+current_budget.get_budget(), font = MEDIUM_FONT)
        total_budget_label.grid(row = 1, column = 1, padx = 15, pady = 15)
        
        weekly_budget_label = ttk.Label(self, text = "Remaining Weekly Budget: "+current_budget.get_weekly_budget(), font = MEDIUM_FONT)
        weekly_budget_label.grid(row = 2, column = 1, padx = 10, pady = 15)
  
        add_income_button = ttk.Button(self, text = "Add Income", command = lambda : [create_new_user, controller.show_frame(incomePage)])
        add_income_button.grid(row = 3, column = 0, padx = 10, pady = 10)

        add_expenses_button = ttk.Button(self, text = "Add Expenses", command = lambda : controller.show_frame(expensePage))
        add_expenses_button.grid(row = 3, column  = 1, padx = 10, pady = 10)

        change_weeks_button = ttk.Button(self, text = "Change No. of Remaing Weeks", command = lambda : controller.show_frame(changeBudgetWeeks))
        change_weeks_button.grid(row = 3, column  = 2, padx = 10, pady = 10)

        delete_button = ttk.Button(self, text = "Delete", command = lambda : [current_user.delete_budget(current_budget.budget_id), self.reset_current_budget(),
                                                                              budgetListPage.load(), controller.show_frame(budgetListPage)])
        delete_button.grid(row = 4, column  = 1, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : [self.reset_current_budget(), budgetListPage.load(), controller.show_frame(budgetListPage)])
        back_button.grid(row = 4, column = 2, padx = 10, pady = 10)
    
    def reset_current_budget(self):
        current_budget = Budget()

    def load():
        week_label.config(text="Weeks Remaining: "+str(current_budget.num_weeks))
        total_budget_label.config(text="Remaining Budget: "+current_budget.get_budget())
        weekly_budget_label.config(text="Remaining Weekly Budget: "+current_budget.get_weekly_budget())

class incomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        add_income_label = ttk.Label(self, text= "Add Income:", font = MEDIUM_FONT)
        add_income_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        income_entry = ttk.Entry(self, text = "Income")
        income_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [current_budget.change_budget, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class expensePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        expense_label = ttk.Label(self, text= "Add Expenses:", font = MEDIUM_FONT)
        expense_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        expense_entry = ttk.Entry(self, text = "Expenses")
        expense_entry.grid(row = 0, column = 2, padx = 15, pady = 10)
  
        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [current_budget.change_budget, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class changeWeeksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        week_label = ttk.Label(self, text= "Current No. of Weeks Remaining:", font = MEDIUM_FONT)
        week_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        new_week_label = ttk.Label(self, text = "Enter New No. of Remaining Weeks:", font = MEDIUM_FONT)
        new_week_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        new_week_entry = ttk.Entry(self, text = "")
        new_week_entry.grid(row = 0, column = 2, padx = 15, pady = 10)
      
        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [change_weeks, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class changeBudgetWeeks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        current_date = str(date.today())
        current_date = tuple(current_date.split('-'))
        print(current_date)
        cal = Calendar(self, selectMode = "day", year = int(current_date[0]), month = int(current_date[1]), day = int(current_date[2]))
        cal.pack(pady = 40, padx = 60)
    

def clear_entry(entry_box):
    entry_box.delete(0, "end")



createDatabase()

db = DatabaseConnection()
app = BudgetApp()
app.mainloop()