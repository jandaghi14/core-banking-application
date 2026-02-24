from tkinter import Frame, Label, Entry, Button, Checkbutton, messagebox
from Presentation.Desktop.UiComponents.password_entry import PasswordEntry
from Business.employee_business import EmployeeBusiness
from Presentation.Desktop.UiComponents.captcha_component import CaptchaComponent

class LoginFrame(Frame):
    def __init__(self, window, employee_business: EmployeeBusiness,view_manager):
        super().__init__(window)

        self.view_manager=view_manager
        self.employee_business = employee_business

        self.grid_columnconfigure(1, weight=1)

        self.header_label = Label(self, text="Login Page")
        self.header_label.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_component = PasswordEntry(self)
        self.password_component.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="ew")

        self.remember_me_checkbutton = Checkbutton(self, text="remember me?")
        self.remember_me_checkbutton.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.captcha = CaptchaComponent(self)
        self.captcha.grid(row=4, column=0,columnspan=2 ,padx=10)


        self.login_button = Button(self, text="Login", command=self.login_button_clicked)
        self.login_button.grid(row=5, column=1, pady=(0, 10), sticky="w")

        self.register_button = Button(self, text="Go to Register", command=self.register_button_clicked)
        self.register_button.grid(row=6, column=1, pady=(0, 10), sticky="w")
        

    def login_button_clicked(self):
        if not self.captcha.validate():
            messagebox.showerror("CAPTCHA Error", "Invalid CAPTCHA! Please try again.")
            self.captcha.refresh_captcha()
            return
        
        username = self.username_entry.get()
        password = self.password_component.get_password_value()
        response = self.employee_business.login(username, password)

        if not response.success:
            messagebox.showerror("Login Failed!", response.message)
        else:
            home_frame = self.view_manager.show_frame('home')
            home_frame.set_current_employee(response.data)

    def register_button_clicked(self):
        self.view_manager.show_frame("register")