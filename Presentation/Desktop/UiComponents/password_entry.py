from tkinter import Frame, Entry, Button
from PIL import Image, ImageTk

class PasswordEntry(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.open_eye = Image.open('Presentation/Desktop/UiComponents/assets/open_eye.png')
        self.open_eye = ImageTk.PhotoImage(self.open_eye)
        
        self.close_eye = Image.open('Presentation/Desktop/UiComponents/assets/close_eye.png')
        self.close_eye = ImageTk.PhotoImage(self.close_eye)

        self.password_visible = False
        
        
        self.grid_columnconfigure(0, weight=1)

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=0, column=0, sticky="ew")

        self.status_button = Button(self, image=self.close_eye, command=self.status_button_clicked)
        self.status_button.grid(row=0, column=1, sticky="w")

    def status_button_clicked(self):
        if not self.password_visible:
            self.status_button.config(image=self.open_eye)
            self.password_entry.config(show="")
            self.password_visible = not self.password_visible
        else:
            self.status_button.config(image=self.close_eye)
            self.password_entry.config(show="*")
            self.password_visible = not self.password_visible

    def get_password_value(self):
        password = self.password_entry.get()
        return password
