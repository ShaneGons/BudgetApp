from datatabase import DatabaseConnection

class User:
    global db
    db = DatabaseConnection()
    def __init__(self):
        self.user_id = -1

    def change_name(self, name):
        pass

    def change_password(self, hash_pass):
        pass

    def get_budgets(self):
        sql = "SELECT budget_id,budget_name,budget,num_weeks FROM tbl_budgets WHERE user_id=?"
        values = (self.user_id,)
        budgets = db.fetch_conditions(sql, values)
        if budgets == None:
            return []
        return budgets
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def delete_budget(self, budget_id):
        pass

    def add_budget(self, budget_name, budget, num_weeks):
        budget_name = str(budget_name)
        budget_name = budget_name.replace(" ", "")
        budget = float(budget)
        budget = round(budget, 2)

        sql = "INSERT INTO tbl_budgets (user_id, budget_name, budget, num_weeks) VALUES (?, ?, ?, ?)"
        values = (self.user_id, budget_name, budget, int(num_weeks))
        if db.execute(sql, values):
            print("Budget created")
            return True
        else:
            print("Error creating budget")
            return False