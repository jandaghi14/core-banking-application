from Common.Enums.roles import Roles
from Common.Enums.statuses import Statuses


class Employee:
    def __init__(self, employee_id, firstname, lastname, username, password, email, phone, status_id,role_id):
        self.id = employee_id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.status = Statuses(status_id)
        self.role = Roles(role_id)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
