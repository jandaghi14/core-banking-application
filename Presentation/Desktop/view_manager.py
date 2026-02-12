from Presentation.Desktop.window import Window
from Presentation.Desktop.Frames.login import LoginFrame
from Presentation.Desktop.Frames.register import RegisterFrame
from Business.employee_business import EmployeeBusiness


class ViewManager:
    def __init__(self, employee_business: EmployeeBusiness):
        self.frames = {}

        self.application_window = Window("Core Banking Application")
        
        self.add_frame("register", RegisterFrame(self.application_window,employee_business,self), 400, 450)
        self.add_frame("login", LoginFrame(self.application_window, employee_business, self), 400  , 300)

        self.application_window.window_resize(f"400x300")

        self.application_window.show()

    def add_frame(self, frame_name, frame, width, height):
        self.frames[frame_name] = {
            "frame": frame,
            "size": f"{width}x{height}"
        }
        frame.grid(row=0, column=0, sticky="ewns")

    def show_frame(self, frame_name):
        frame_data = self.frames[frame_name]
        frame = frame_data["frame"]
        frame_size = frame_data["size"]

        frame.tkraise()
        self.application_window.window_resize(frame_size)
