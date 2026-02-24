from abc import ABC, abstractmethod


class IEmployeeRepository(ABC):
    @abstractmethod
    def get_employee_by_username_password(self, username: str, password: str):
        pass

    @abstractmethod
    def insert_new_employee(self,firstname, lastname, username,password,email, employee_status_id,role_id):
        pass

    @abstractmethod
    def get_employee_by_username(self, username):
        pass

    @abstractmethod
    def update_employee(self, employee_id, firstname, lastname,username,email, status_id, role_id):
        pass
    
    @abstractmethod
    def update_password(self, employee_id, new_password):
        pass
    
    
