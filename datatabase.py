import sqlite3

class DatabaseConnection:

    def createDatabase():
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS tbl_users (
                            user_id INTEGER PRIMARY KEY,
                            f_name TEXT NOT NULL,
                            password TEXT NOT NULL
                        );""")
            
            #final_week is the data the user wants the budget to last till
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_budgets (
                            budget_id INTEGER PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            budget REAL NOT NULL,
                            final_week TEXT NOT NULL
                            FOREIGN KEY (user_id) REFERENCES tbl_users (user_id)
                        );""")
            c.close()

            return True
        except:
            print("Error creating database")
            return False

    def fetch(self,sql):
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute(sql)
            request = c.fetchall()
            c.close()

            return request
        except:
            print("Error fetching data")
            return None
    
    def execute(self,sql):
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute(sql)
            conn.commit()
            c.close()
            
            return True
        except:
            print("Error updating database")
            return False