from tkinter import Tk


class Window(Tk):
    def __init__(self, application_title):
        super().__init__()

        self.title(application_title)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def window_resize(self, value):
        self.geometry(value)

    def show(self):
        self.mainloop()
