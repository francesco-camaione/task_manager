from datetime import datetime
from pymysqlpool import ConnectionPool
 
class Database:

    def __init__(self, database="task_manager", user="root", password="", hostname="127.0.0.1"):
        self.pool = ConnectionPool(
            host=hostname,
            user=user,
            passwd=password,
            database=database,
            port=3306,
            autocommit=True
            # charset="utf8mb4",
            # buffered=True
        )

    # just execute query
    def _execute_(self, query):
        connection = self.pool.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
        connection.close()
    
    # execute query and return first element of the result
    def _execute_one_(self, query):
        result = self._execute_all_(query)
        return result[0] if len(result) > 0 else None

    # execute query and return all results
    def _execute_all_(self, query):
        connection = self.pool.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        connection.close()
        return result
    
    def check_auth(self, ksuid: int):
        res = self._execute_one_(f"SELECT * FROM Users WHERE ksuid={ksuid} LIMIT 1")
        return res is not None 


    def create_user(self, ksuid: str, email: str, pswrd: str, created_at: datetime):
        user_exist = self._execute_one_(f"SELECT * FROM Users WHERE ksuid =\"{ksuid}\" ")
        if not user_exist:
            self._execute_(f"INSERT INTO Users (ksuid, email, pswrd, created_at) VALUES (\"{ksuid}\", \"{email}\", \"{pswrd}\", \"{created_at}\")")
            return "User created"
        return "This user already exists"
            

    def delete_user(self, ksuid):
        self._execute_(f"DELETE FROM Users WHERE ksuid={ksuid}")

    def create_task(self, id, description, priority):
        task_exist = self._execute_one_(f"SELECT * FROM Tasks WHERE id={id}")
        if not task_exist:
            self._execute_(f"INSERT INTO Tasks (id, description, priority_1to5) VALUES (\"{id}\", \"{description}\", \"{priority}\")")
            return "Task created"
        return "Task already created"

    def delete_task(self, id: int):
        self._execute_(f"DELETE FROM Tasks WHERE id={id}")
