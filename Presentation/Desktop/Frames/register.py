from tkinter import Frame, Label,Entry,Button, messagebox
from Business.employee_business import EmployeeBusiness
from Presentation.Desktop.UiComponents.password_entry import PasswordEntry
from Presentation.Desktop.UiComponents.captcha_component import CaptchaComponent




class RegisterFrame(Frame):
    def __init__(self, window, employee_business:EmployeeBusiness,view_manager):
        super().__init__(window)
        self.view_manager= view_manager
        self.employee_business= employee_business
        
        self.grid_columnconfigure(1,weight=1)

        self.header_label = Label(self, text="Register Page")
        self.header_label.grid(row=0, column=1, pady=10, sticky="w")
        
        self.label_firstname = Label(self, text='First Name:')
        self.label_firstname.grid(row=1,column=0,padx=10,pady=(0,10),sticky='nes')
        self.entry_firstname= Entry(self)
        self.entry_firstname.grid(row=1, column=1, pady=(0,10), padx=(0,10),sticky='we')
        
        self.label_lastname = Label(self, text='Last Name:')
        self.label_lastname.grid(row=2,column=0,padx=10,pady=(0,10),sticky='e')
        self.entry_lastname= Entry(self)
        self.entry_lastname.grid(row=2, column=1, pady=(0,10),padx=(0,10),sticky='we')
        
        self.label_username = Label(self, text='User Name:')
        self.label_username.grid(row=3,column=0,padx=10,pady=(0,10),sticky='e')
        self.entry_username= Entry(self)
        self.entry_username.grid(row=3, column=1, pady=(0,10),padx=(0,10),sticky='we')
        
        self.label_password = Label(self, text='Password:')
        self.label_password.grid(row=5,column=0,padx=10,pady=(0,10),sticky='e')
        self.entry_password= PasswordEntry(self)
        self.entry_password.grid(row=5, column=1, pady=(0,10),padx=(0,10),sticky='we')

        self.captcha= CaptchaComponent(self)
        self.captcha.grid(row=6,column=0,columnspan=2,pady=10)

        self.label_email = Label(self, text='Email:')
        self.label_email.grid(row=4,column=0,padx=10,pady=(0,10),sticky='e')
        self.entry_email= Entry(self)
        self.entry_email.grid(row=4, column=1, pady=(0,10),padx=(0,10),sticky='we')


        self.register_button = Button(self, text="Register!", command=self.register_button_clicked)
        self.register_button.grid(row=7, column=0,padx=10, pady=(0, 10), sticky="w")

        self.goto_login_button = Button(self, text="Go to Login!", command=self.clicked_go_to_login)
        self.goto_login_button.grid(row=8, column=0,padx=10, pady=(0, 10), sticky="w")

    
    
    def register_button_clicked(self):
        if not self.captcha.validate():
            messagebox.showerror("CAPTCHA Error", "Invalid CAPTCHA! Please try again.")
            self.captcha.refresh_captcha()
            return
        
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get_password_value()
        
        response= self.employee_business.register(firstname, lastname, username,password,email)
        
        if response.success:
            messagebox.showinfo("Register Successfully!", response.message)
            self.entry_firstname.delete(0, 'end')
            self.entry_lastname.delete(0, 'end')
            self.entry_username.delete(0, 'end')
            self.entry_password.password_entry.delete(0, 'end')
            self.view_manager.show_frame('login')
        else:
            messagebox.showerror("Register Failed", response.message)   
    
    def clicked_go_to_login(self):
        self.view_manager.show_frame("login")