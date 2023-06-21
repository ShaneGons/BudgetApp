from datatabase import DatabaseConnection

class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def change_name():
        pass

    def change_password():
        pass

    def get_budgets(self):
        db = DatabaseConnection()
        budgets = db.fetch("SELECT budget_id,budget,final_week FROM tbl_budgets WHERE user_id="+self.user_id+";")
        return budgets