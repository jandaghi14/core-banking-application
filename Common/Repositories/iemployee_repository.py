from abc import ABC, abstractmethod


class IEmployeeRepository(ABC):
    @abstractmethod
    def get_employee_by_username_password(self, username: str, password: str):
        pass

    @abstractmethod
    def insert_new_employee(self):
        pass

    @abstractmethod
    def get_employee_by_username(self):
        pass

    
