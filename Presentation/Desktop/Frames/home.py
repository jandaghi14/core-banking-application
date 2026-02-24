from tkinter import Frame, Label, Button
from Common.Entities.employee import Employee
from Common.Enums.roles import Roles


class HomeFrame(Frame):
    def __init__(self, window, view_manager):
        super().__init__(window)
        self.current_employee = None
        self.view_manager = view_manager

        self.grid_columnconfigure(0, weight=1)

        self.header_label = Label(self)
        self.header_label.grid(row=0, column=0, pady=10, padx=10)

        self.profile_button = Button(self, text="My Profile", command=self.profile_clicked)
        self.profile_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.account_management_button = Button(self, text="Accounts Management", command=self.accounts_management)

        
        self.logout_button = Button(self, text="Logout", command = self.login_page_clicked)
        self.logout_button.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="ew")

    def login_page_clicked(self):
        self.view_manager.show_frame('login')
        
    def set_current_employee(self, employee: Employee):
            self.current_employee = employee
            self.header_label.config(text=f"Welcome {employee.get_fullname()}")
            match employee.role:
                case Roles.admin:
                    self.account_management_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ew")
                case Roles.banker:
                    self.account_management_button.grid_forget()
    
    def profile_clicked(self):
        profile_frame = self.view_manager.show_frame('profile')
        profile_frame.set_current_employee(self.current_employee)
        

    def accounts_management(self):
        pass