from tkinter import Toplevel,Label, Button, Entry, messagebox
from Presentation.Desktop.UiComponents.password_entry import PasswordEntry
from datetime import datetime, timedelta,timezone
from hashlib import md5

class ResetPassword(Toplevel):
    def __init__(self, parent, employee_business, employee):
        super().__init__(parent)
        self.current_employee = employee
        self.employee_business = employee_business
        self.reset_code = None
        self.time = None
        
        
        self.title('Reset Password')
        self.geometry('400x400')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        Label(self, text="Reset Password").grid(row=0, column=0, columnspan=2, padx=10, pady=(15,5), sticky="w")

        Label(self, text="Old Password:").grid(row=1, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_old_password = PasswordEntry(self)
        self.entry_old_password.grid(row=1, column=1, padx=10, pady=(0,5), sticky="ew")

        Label(self, text="New Password:").grid(row=3, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_new_password = PasswordEntry(self)
        self.entry_new_password.grid(row=3, column=1, padx=10, pady=(0,5), sticky="ew")

        Button(self, text="Send Email", command=self.send_email_clicked).grid(row=5, column=0, padx=10, pady=(10,5), sticky="ew")
        Button(self, text="Send SMS", command=self.send_sms_clicked).grid(row=5, column=1, padx=10, pady=(10,5), sticky="ew")

        Label(self, text="Code:").grid(row=6, column=0, padx=10, pady=(0,5), sticky="e")
        self.entry_code = Entry(self)
        self.entry_code.grid(row=6, column=1, padx=10, pady=(0,5), sticky="ew")

        Button(self, text="Submit", command=self.submit_button_clicked).grid(row=7, column=1, padx=10, pady=10, sticky="w")
        Button(self, text="Back", command=self.back_button_clicked).grid(row=8, column=1, padx=10, pady=(0,10), sticky="w")

    def send_email_clicked(self):
        old_password = self.entry_old_password.get_password_value()
        response = self.employee_business.verify_old_password(self.current_employee,old_password)
        if response.success:
            self.time = datetime.now()
            response = self.employee_business.send_reset_code(self.current_employee)
            messagebox.showinfo("Success", "Code sent to your email!")  # add this
            self.reset_code = response.data
        else:
            messagebox.showerror("Error", response.message)
            
            

    def send_sms_clicked(self):
        pass

    def submit_button_clicked(self):
        if not self.reset_code:
            messagebox.showerror("Error", "Please request a code first.")
            return
        if self.entry_code.get().upper() == self.reset_code and datetime.now() < self.time + timedelta(minutes=2):
                response = self.employee_business.reset_password(self.current_employee, self.entry_new_password.get_password_value())
                messagebox.showinfo('Password' , response.message)
                self.destroy()
        else:
            messagebox.showerror("Error", "Invalid or expired code.")
    def back_button_clicked(self):
        self.destroy()
