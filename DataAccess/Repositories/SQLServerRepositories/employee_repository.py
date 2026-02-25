import pymssql
from Common.Repositories.iemployee_repository import IEmployeeRepository
from Common.Entities.employee import Employee


class SQLServerEmployeeRepository(IEmployeeRepository):
    def __init__(self,database_name):
        super().__init__()
        self.database_name = database_name
    
    def create_connection(self):
        return pymssql.connect(host='localhost\PythonDBAsus',database=self.database_name)

    def get_employee_by_username_password(self, username: str, password: str):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
              SELECT   Id,
                       FirstName,
                       LastName,
                       Username,
                       Password,
                       Email,
                       Phone,
                       StatusId,
                       RoleId
              FROM     Employee
              Where    Username    =    %s 
              AND      Password    =    %s """, (username, password))
            row = cursor.fetchone()
            if row:
                employee = Employee(*row)
                return employee

    def get_employee_by_username(self, username):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
              SELECT   Id,
                       FirstName,
                       LastName,
                       Username,
                       Password,
                       Email,
                       Phone,
                       StatusId,
                       RoleId
              FROM     Employee
              Where    Username    =    %s
              """, (username,))
            row = cursor.fetchone()
            if row:
                employee = Employee(*row)
                return employee
            else:
                return None    

    def insert_new_employee(self, firstname, lastname, username,password,email, phone, employee_status_id=2,role_id=1):
        with self.create_connection() as connection:
            cursor= connection.cursor()
            cursor.execute("""
                           INSERT INTO Employee (
                                    FirstName,
                                    LastName,
                                    Username,
                                    Password,
                                    Email,
                                    Phone,
                                    StatusId,
                                    RoleId
                     )
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                           """,(firstname,lastname,username,password,email,phone,employee_status_id,role_id))
            connection.commit()
            return True
        
        
    def update_employee(self, employee_id, firstname, lastname, username,email, phone, status_id, role_id):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                           UPDATE [dbo].[Employee]
                            SET [FirstName] = %s
                                ,[LastName] = %s
                                ,[Username] = %s
                                ,[Email] = %s
                                ,[Phone] = %s
                                ,[StatusId] = %s
                                ,[RoleId] = %s
                            WHERE id = %s
                           """,(firstname, lastname, username, email, phone, status_id, role_id, employee_id))
            connection.commit()
    
    def update_password(self, employee_id, new_password):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Employee SET Password = %s WHERE Id = %s
            """, (new_password, employee_id))
            connection.commit()