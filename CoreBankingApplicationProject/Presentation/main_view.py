from Presentation.window import Window
from Presentation.Frames.login import LoginFrame
from Presentation.Frames.register import RegisterFrame
from Presentation.Frames.otp import OtpFrame
from tkinter import Frame




class MainView:
    def __init__(self,user_business):
        self.frames = {}

        self.window = Window("Core Banking")

        self.user_business = user_business

        self.add_frame("register", RegisterFrame(self.window, self), 400, 420)
        self.add_frame("login", LoginFrame(self.window, self,user_business), 400, 320)

        self.show_frame("login")

        self.window.show()

    def add_frame(self, frame_name: str, frame: Frame, width, height):
        self.frames[frame_name] = (frame, width, height)
        self.frames[frame_name][0].grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name: str):
        current_frame_value = self.frames[frame_name]
        current_frame_value[0].tkraise()

        width, height = current_frame_value[1], current_frame_value[2]

        self.window.resize(width, height)

    def show_otp_frame(self, mobile: str):
        otp_frame = OtpFrame(self.window, self, mobile)
        self.add_frame("otp", otp_frame, 400, 280)
        self.show_frame("otp")