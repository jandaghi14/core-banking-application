class Employee:
    def __init__(self, employee_id, firstname, lastname, username, password, status_id):
        self.id = employee_id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.status_id = status_id

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
