import sqlite3
from Common.Repositories.iemployee_repository import IEmployeeRepository
from Common.Entities.employee import Employee


class SQLiteEmployeeRepository(IEmployeeRepository):
    def __init__(self, database_name):
        self.database_name = database_name

    def create_connection(self):
        return sqlite3.connect(self.database_name)

    def get_employee_by_username_password(self, username: str, password: str):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
              SELECT   Id,
                       FirstName,
                       LastName,
                       Username,
                       Password,
                       EmployeeStatusId
              FROM     Employee
              Where    Username    =    ?
              AND      Password    =    ?""", (username, password))
            row = cursor.fetchone()
            if row:
                employee = Employee(*row)
                return employee

    def get_employee_by_username(self, username):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
              SELECT   *
              FROM     Employee
              Where    Username    =    ?
              """, (username,))
            row = cursor.fetchone()
            if row:
                employee = Employee(*row)
                return employee
            else:
                return None
    
    
    def insert_new_employee(self, firstname, lastname, username,password,employee_status_id=2):
        with self.create_connection() as connection:
            cursor= connection.cursor()
            cursor.execute("""
                           INSERT INTO Employee (
                                    FirstName,
                                    LastName,
                                    Username,
                                    Password,
                                    EmployeeStatusId
                     )
                     VALUES (?,?,?,?,?)
                           """,(firstname,lastname,username,password,employee_status_id))
            connection.commit()
            return True

    