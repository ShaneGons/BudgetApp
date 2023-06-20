import sqlite3

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
    
    def execute(self,sql):
        try:
            conn = sqlite3.connect('budget.db')
            c = conn.cursor()

            c.execute(sql)
            conn.commit()
            c.close()

        except:
            print("Error updating database")
            return None