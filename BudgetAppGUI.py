import tkinter as tk
from tkinter import ttk
from BudgetFunctions import *
import User
import Budget

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

        for F in (loginPage, registerPage, budgetListPage, mainMenuPage, incomePage, expensePage, changeWeeksPage):
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
        
        name_label = ttk.Label(self, text= "Name:", font = LARGE_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = LARGE_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        login_button = ttk.Button(self, text = "Login", command = lambda : [get_user(name_entry.get(), password_entry.get()), clear_entry(name_entry), clear_entry(password_entry), controller.show_frame(budgetListPage)])
        login_button.grid(row = 4, column = 2, padx = 10, pady = 10)
  
        register_button = ttk.Button(self, text = "Register", command = lambda : controller.show_frame(registerPage))
        register_button.grid(row = 4, column = 4, padx = 10, pady = 10)
    



class registerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        name_label = ttk.Label(self, text= "Name:", font = LARGE_FONT)
        name_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        name_entry = ttk.Entry(self, text = "Name")
        name_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        password_label = ttk.Label(self, text = "Password:", font = LARGE_FONT)
        password_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        password_entry = ttk.Entry(self, show = "*")
        password_entry.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        register_button = ttk.Button(self, text = "Register", command = lambda : [create_new_user, clear_entry(name_entry), clear_entry(password_entry), controller.show_frame(loginPage)])
        register_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(loginPage))
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

        select_button = ttk.Button(self, text = "Select", command = lambda : [self.run_budget, controller.show_frame(mainMenuPage)])
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
            # budget = Budget(budget_id, values[1], values[2])

    
    def back(self):
        current_user = None


class mainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        week_label = ttk.Label(self, text= "Weeks Remaining:", font = LARGE_FONT)
        week_label.grid(row = 0, column = 1, padx = 10, pady = 10)

        weekly_budget_label = ttk.Label(self, text = "Remaining Weekly Budget:", font = LARGE_FONT)
        weekly_budget_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        total_budget_label = ttk.Label(self, text = "Remaining Budget:", font = LARGE_FONT)
        total_budget_label.grid(row = 1, column = 2, padx = 15, pady = 10)
  
        add_income_button = ttk.Button(self, text = "Add Income", command = lambda : [create_new_user, controller.show_frame(incomePage)])
        add_income_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        add_expenses_button = ttk.Button(self, text = "Add Expenses", command = lambda : controller.show_frame(expensePage))
        add_expenses_button.grid(row = 4, column  = 3, padx = 10, pady = 10)

        change_weeks_button = ttk.Button(self, text = "Change No. of Remaing Weeks", command = lambda : controller.show_frame(changeWeeksPage))
        change_weeks_button.grid(row = 4, column  = 3, padx = 10, pady = 10)

        delete_button = ttk.Button(self, text = "Delete", command = lambda : [delete_budget, controller.show_frame(budgetListPage)])
        delete_button.grid(row = 4, column  = 3, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(budgetListPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class incomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        add_income_label = ttk.Label(self, text= "Add Income:", font = LARGE_FONT)
        add_income_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        income_entry = ttk.Entry(self, text = "Income")
        income_entry.grid(row = 0, column = 2, padx = 15, pady = 10)

        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [budget.change_budget, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class expensePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        expense_label = ttk.Label(self, text= "Add Expenses:", font = LARGE_FONT)
        expense_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        expense_entry = ttk.Entry(self, text = "Expenses")
        expense_entry.grid(row = 0, column = 2, padx = 15, pady = 10)
  
        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [budget.change_budget, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)


class changeWeeksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        week_label = ttk.Label(self, text= "Current No. of Weeks Remaining:", font = LARGE_FONT)
        week_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        new_week_label = ttk.Label(self, text = "Enter New No. of Remaining Weeks:", font = LARGE_FONT)
        new_week_label.grid(row = 1, column = 1, padx = 10, pady = 10)

        new_week_entry = ttk.Entry(self, text = "")
        new_week_entry.grid(row = 0, column = 2, padx = 15, pady = 10)
      
        confirm_button = ttk.Button(self, text = "Confirm", command = lambda : [change_weeks, controller.show_frame(mainMenuPage)])
        confirm_button.grid(row = 4, column = 2, padx = 10, pady = 10)

        back_button = ttk.Button(self, text = "Back", command = lambda : controller.show_frame(mainMenuPage))
        back_button.grid(row = 4, column = 4, padx = 10, pady = 10)

def clear_entry(entry_box):
    entry_box.delete(0, "end")

current_user = None
budget = None

app = BudgetApp()
app.mainloop()