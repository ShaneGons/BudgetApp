from datatabase import DatabaseConnection

class User:
    def __init__(self):
        self.user_id = -1

    def change_name(self):
        pass

    def change_password(self):
        pass

    def get_budgets(self):
        db = DatabaseConnection()
        budgets = db.fetch("SELECT budget_id,budget,num_weeks FROM tbl_budgets WHERE user_id=?", (self.user_id))
        return budgets
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_budgets(self):
        return []