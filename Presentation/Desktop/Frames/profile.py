from tkinter import Frame, Label, Entry, Button
from Common.Entities.employee import Employee
from Common.Enums.roles import Roles

class ProfileFrame(Frame):
    def __init__(self, window, view_manager):
        super().__init__(window)
        self.current_employee = None
        self.view_manager = view_manager
        self.grid_columnconfigure(1, weight=1)

        Label(self, text="First Name:").grid(row=0, column=0, padx=10, pady=(10,5), sticky="e")
        self.entry_firstname = Entry(self)
        self.entry_firstname.grid(row=0, column=1, padx=10, pady=(10,5), sticky="ew")

        Label(self, text="Last Name:").grid(row=1, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_lastname = Entry(self)
        self.entry_lastname.grid(row=1, column=1, padx=10, pady=(0,5), sticky="ew")

        Label(self, text="Username:").grid(row=2, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_username = Entry(self)
        self.entry_username.grid(row=2, column=1, padx=10, pady=(0,5), sticky="ew")
        
        Label(self, text="Email:").grid(row=3, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_email = Entry(self)
        self.entry_email.grid(row=3, column=1, padx=10, pady=(0,5), sticky="ew")

        Label(self, text="Status:").grid(row=4, column=0, padx=10, pady=(0,5), sticky="e")
        self.label_status = Label(self, text="-")
        self.label_status.grid(row=4, column=1, padx=10, pady=(0,5), sticky="w")

        Label(self, text="Role:").grid(row=5, column=0, padx=10, pady=(0,5), sticky="e")
        self.label_role = Label(self, text="-")
        self.label_role.grid(row=5, column=1, padx=10, pady=(0,5), sticky="w")

        self.edit_button = Button(self, text="Edit", command=self.edit_button_clicked)
        self.edit_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        
        self.back_button = Button(self, text="Back", command=self.back_button_clicked)
        self.back_button.grid(row=7, column=1, padx=10, pady=(0,10), sticky="w")

    def edit_button_clicked(self):
        edit_profile_frame = self.view_manager.show_frame('edit_profile')
        edit_profile_frame.set_current_employee(self.current_employee)

    def set_current_employee(self, employee:Employee):
        self.entry_firstname.config(state="normal")
        self.entry_firstname.delete(0, 'end')
        self.entry_firstname.insert(0, employee.first_name)
        self.entry_firstname.config(state="readonly")

        self.entry_lastname.config(state="normal")
        self.entry_lastname.delete(0, 'end')
        self.entry_lastname.insert(0, employee.last_name)
        self.entry_lastname.config(state="readonly")

        self.entry_username.config(state="normal")
        self.entry_username.delete(0, 'end')
        self.entry_username.insert(0, employee.username)
        self.entry_username.config(state="readonly")

        self.entry_email.config(state="normal")
        self.entry_email.delete(0, 'end')
        self.entry_email.insert(0, employee.email)
        self.entry_email.config(state="readonly")
        
        

        self.label_status.config(text=employee.status.name)
        self.label_role.config(text=employee.role.name)
        
        self.current_employee = employee
        
        match employee.role:
            case Roles.admin:
                self.edit_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")
            case Roles.banker:
                self.edit_button.grid_forget()
    
    def back_button_clicked(self):
        self.view_manager.show_frame('home')