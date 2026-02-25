from tkinter import Frame, Label, Entry, Button, messagebox
from tkinter import ttk
from Common.Entities.employee import Employee
from Presentation.Desktop.UiComponents.password_entry import PasswordEntry
from Presentation.Desktop.UiComponents.reset_password import ResetPassword
from Common.Enums.statuses import Statuses
from Common.Enums.roles import Roles


class EditProfileFrame(Frame):
    def __init__(self, window, view_manager, employee_business):
        super().__init__(window)
        self.employee_business = employee_business
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

        Label(self, text="Phone:").grid(row=4, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_phone = Entry(self)
        self.entry_phone.grid(row=4, column=1, padx=10, pady=(0,5), sticky="ew")

        Label(self, text="Status:").grid(row=5, column=0, padx=10, pady=(0,5), sticky="e")
        self.combo_status = ttk.Combobox(self, state='readonly')
        self.combo_status.grid(row=5, column=1, padx=10, pady=(0,5), sticky="ew")
        self.combo_status['values'] = [s.name for s in Statuses]


        Label(self, text="Role:").grid(row=6, column=0, padx=10, pady=(0,5), sticky="e")
        self.combo_role = ttk.Combobox(self, state='readonly')
        self.combo_role.grid(row=6, column=1, padx=10, pady=(0,5), sticky="ew")
        self.combo_role['values'] = [r.name for r in Roles]


        Button(self, text="Reset Password", command=self.reset_password_clicked).grid(row=10, column=1, padx=10, pady=10, sticky="w")
        
        Button(self, text="Submit", command=self.submit_button_clicked).grid(row=11, column=1, padx=10, pady=10, sticky="w")
        Button(self, text="Back", command=self.back_button_clicked).grid(row=12, column=1, padx=10, pady=(0,10), sticky="w")


    def reset_password_clicked(self):
        ResetPassword(self, self.employee_business, self.current_employee)
    
    
    def send_email_clicked(self):
        pass

    def send_sms_clicked(self):
        pass

    def submit_button_clicked(self):
        firstname = self.entry_firstname.get() 
        lastname = self.entry_lastname.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        status_id = Statuses[self.combo_status.get()].value
        role_id = Roles[self.combo_role.get()].value
        response = self.employee_business.update_employee(self.current_employee.id, firstname, lastname, username, email, phone, status_id, role_id)
        if response.success:
            self.current_employee.first_name = firstname
            self.current_employee.last_name = lastname
            self.current_employee.username = username
            self.current_employee.email = email
            self.current_employee.phone = phone
            self.current_employee.status_id = status_id
            self.current_employee.role = Roles(role_id)
            messagebox.showinfo("Success", response.message)
            self.view_manager.show_frame('profile')
            
        else:
            messagebox.showerror("Error", response.message)
                

    def back_button_clicked(self):
        self.view_manager.show_frame('profile')

    def set_current_employee(self, employee: Employee):
        self.current_employee = employee
        self.entry_firstname.delete(0, 'end')
        self.entry_firstname.insert(0, employee.first_name)

        self.entry_lastname.delete(0, 'end')
        self.entry_lastname.insert(0, employee.last_name)

        self.entry_username.delete(0, 'end')
        self.entry_username.insert(0, employee.username)
        
        self.entry_email.delete(0, 'end')
        self.entry_email.insert(0, employee.email)
        
        self.entry_phone.delete(0, 'end')
        self.entry_phone.insert(0, employee.phone)

        self.combo_status.set(employee.status.name)
        self.combo_role.set(employee.role.name)