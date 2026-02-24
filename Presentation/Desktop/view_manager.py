from Presentation.Desktop.window import Window
from Presentation.Desktop.Frames.login import LoginFrame
from Presentation.Desktop.Frames.register import RegisterFrame
from Presentation.Desktop.Frames.home import HomeFrame

from Presentation.Desktop.Frames.profile import ProfileFrame
from Presentation.Desktop.Frames.edit_profile import EditProfileFrame
from Business.employee_business import EmployeeBusiness

from Common.Entities.employee import Employee


class ViewManager:
    def __init__(self, employee_business: EmployeeBusiness):
        self.frames = {}

        self.application_window = Window("Core Banking Application")
        
        
        self.add_frame('edit_profile',EditProfileFrame(self.application_window,self, employee_business),400, 450)
        self.add_frame('home',HomeFrame(self.application_window, self),400,450)
        self.add_frame("register", RegisterFrame(self.application_window,employee_business ,self), 400, 450)
        self.add_frame("profile", ProfileFrame(self.application_window ,self), 400, 450)
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
        
        return frame
