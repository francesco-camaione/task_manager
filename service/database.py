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

    # def __del__(self):
    #     self.pool._remove_connections()

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

    def create_user(self, ksuid, email, pswrd, created_at):
        self.database._execute_(f"INSERT INTO Users (ksuid, email, pswrd, created_at) VALUES ({ksuid}, {email}, {pswrd}, {created_at})")

    def delete_user(self, ksuid):
        self.database._execute_(f"DELETE FROM Users WHERE ksuid={ksuid}")

    def create_task(self):
        self.database._execute_(f"INSERT INTO Tasks (ksuid, email, pswrd, created_at) VALUES ({ksuid}, {email}, {pswrd}, {created_at})")

    def delete_task(self):
        self.database._execute_
