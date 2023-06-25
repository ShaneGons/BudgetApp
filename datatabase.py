import sqlite3

def createDatabase():
        try:
            conn = sqlite3.connect('budget.db') 
            c = conn.cursor()

            #user_id - unique identifier for each user
            #name - name of user
            #password - hashed password
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            password TEXT NOT NULL
                        );""")
            
            #budget_id - unique identifier for each budget
            #user_id - foreign key that associates a budget with a user
            #budget - the remaining budget
            #num_weeks - the remaining no. of weeks the budget needs to last for
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_budgets (
                            budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            budget REAL NOT NULL,
                            num_weeks INTEGER NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES tbl_users (user_id)
                        );""")
            c.close()
            print("Table created")
            return True
        except Exception as e:
            print(e)
            return False
        
class DatabaseConnection:

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
        
    def fetch_conditions(self,sql, values):
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute(sql, values)
            request = c.fetchall()
            c.close()

            return request
        except:
            print("Error fetching data")
            return None
    
    def execute(self,sql,values):
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute(sql, values)
            conn.commit()
            c.close()
            
            return True
        except:
            print("Error updating database")
            return False