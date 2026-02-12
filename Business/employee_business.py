from Common.DTO.reponse import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository
import hashlib


class EmployeeBusiness:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def login(self, username, password):
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid data for username or password.", None)

        hash_password = hashlib.md5(password.encode()).hexdigest()
        employee = self.employee_repository.get_employee_by_username_password(username, hash_password)

        if not employee:
            return Response(False, "Invalid username or password.", None)

        if employee.status_id == 2:
            return Response(True, f"Welcome {employee.get_fullname()}", employee)
        elif employee.status_id == 1:
            return Response(False, "your account is pending status.", None)
        elif employee.status_id == 3:
            return Response(False, "your account is deactive.", None)
    
    def register(self, firstname, lastname, username,password):
        employee = self.employee_repository.get_employee_by_username(username)
        if employee:
            return Response(False,f'Username {employee.username} exists in database!', employee)
        
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid data for username or password.", None)
        
        hash_password = hashlib.md5(password.encode()).hexdigest()
        employee = self.employee_repository.insert_new_employee(firstname, lastname, username,hash_password)
        if employee:
            return Response(True, f'Employee with username {username} added to database.',None)    
        
