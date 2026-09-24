from tkinter import Frame, Label, Entry, Button, messagebox
from Common.Services.sms_service import SmsService


class OtpFrame(Frame):
    def __init__(self, main_window, main_view, mobile: str):
        super().__init__(main_window)

        self.main_view = main_view
        self.mobile = mobile
        self.sms_service = SmsService()
        self.correct_code = None

        self.remaining_seconds = 0
        self.timer_job = None

        self.grid_columnconfigure(1, weight=1)

        self.welcome_label = Label(self, text="Enter the code sent to your phone")
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(15, 10), padx=10)

        self.code_label = Label(self, text="Code")
        self.code_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

        self.code_entry = Entry(self)
        self.code_entry.grid(row=1, column=1, pady=10, padx=(0, 10), sticky="ew")

        self.validation_button = Button(self, text="Validation", command=self.validation_button_clicked)
        self.validation_button.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.retry_button = Button(self, text="Send Retry SMS", command=self.retry_button_clicked)
        self.retry_button.grid(row=3, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.timer_label = Label(self, text="")
        self.timer_label.grid(row=4, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        self.send_initial_otp()

    def send_initial_otp(self):
        self.correct_code = self.sms_service.generate_code()
        self.sms_service.send_otp(self.mobile, self.correct_code)
        self.start_timer(120)

    def validation_button_clicked(self):
        user_code = self.code_entry.get().strip()

        if user_code == self.correct_code:
            messagebox.showinfo("Success", "OTP verified successfully!")
        else:
            messagebox.showerror("Validation Failed", "The code you entered is incorrect.")

    def retry_button_clicked(self):
        if self.remaining_seconds > 0:
            return

        self.correct_code = self.sms_service.generate_code()
        self.sms_service.send_otp(self.mobile, self.correct_code)
        self.start_timer(120)

    def start_timer(self, seconds: int):
        self.remaining_seconds = seconds
        self.retry_button.config(state="disabled")
        self.update_timer()

    def update_timer(self):
        if self.remaining_seconds > 0:
            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60
            self.timer_label.config(text=f"Retry available in {minutes}:{seconds:02d}")
            self.remaining_seconds -= 1
            self.timer_job = self.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="")
            self.retry_button.config(state="normal")