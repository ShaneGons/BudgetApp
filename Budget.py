from datatabase import DatabaseConnection

class Budget:
    
    def __init__(self):
        self.budget_id = -1
        self.budget = -1
        self.num_weeks = -1

    def add_income(self, income): #will add user's income to their total budget
        self.budget += income

    def enter_expenses(self, expenses): #will take user to screen to input their spending
        self.budget -= expenses

    def change_final_week(self, new_num_weeks): #will allow user to change how long their budget needs to last
        if new_num_weeks < 1:
            return False
        db = DatabaseConnection()
        return db.execute("UPDATE Budgets SET num_weeks=? WHERE budgetID=?", (new_num_weeks, self.budget_id))
    
    def set_budget_id(self, budget_id):
        self.budget_id = budget_id

    def set_budget(self, budget):
        self.budget = budget

    def set_num_weeks(self, num_weeks):
        self.num_weeks = num_weeks
    
    def get_budget(self):
        return "{:.2f}".format(self.budget)
    
    def get_weekly_budget(self):
        week_budget = self.budget/self.num_weeks
        return "{:.2f}".format(week_budget)
        
