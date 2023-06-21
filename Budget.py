from datatabase import DatabaseConnection

class Budget:

    
    def __init__(self, budget_id, budget, final_week):
        self.budget_id = budget_id
        self.budget = budget
        self.final_week = final_week

    def add_income(self, income): #will add user's income to their total budget
        pass

    def enter_expenses(self, expenses): #will take user to screen to input their spending
        pass

    def change_final_week(self, new_week): #will allow user to change how long their budget needs to last
        if new_week < 1:
            return False
        db = DatabaseConnection()
        return db.execute("UPDATE Budgets SET final_week="+new_week+" WHERE budgetID="+self.budget_id+";")
        
