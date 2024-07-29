import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
import Owner_Dashboard
import firebase_connection
import landingPage


class SignupClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Admin sign up")
        self.root.state("zoom")
        self.root.configure(background='lightblue')

        self.user32 = ctypes.windll.user32
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)

        self.image = Image.open("risen-wang-20jX9b35r_M-unsplash.jpg")
        self.image = self.image.resize((self.screen_width, self.screen_height))
        self.image = ImageTk.PhotoImage(self.image)

        self.bg_label = tk.Label(self.root, image=self.image)
        self.bg_label.place(relwidth=1, relheight=1)

        def prevPage():
            self.root.destroy()
            landingPage.LandingPageClass()

        self.prev_button = tk.Button(self.root, command=prevPage, text=" < ", background='pink')
        self.prev_button.place(x=10, y=15)

        self.username_label = tk.Label(self.root, text="Username:", font=10, background='gray', foreground='white', bd=35)
        self.password_label = tk.Label(self.root, text="Password:", font=10, background='gray', foreground='white', bd=35)
        self.confirm_password_label = tk.Label(self.root, text="Confirm Password:", font=10, background='gray', foreground='white', bd=35)

        self.username_entry = tk.Entry(self.root, width=25, font=10, highlightthickness=2, highlightbackground='black', bd=3)
        self.password_entry = tk.Entry(self.root, show="*", width=25, font=10, highlightthickness=2, highlightbackground='black', bd=3)
        self.confirm_password_entry = tk.Entry(self.root, show="*", width=25, font=10, highlightthickness=2, highlightbackground='black', bd=3)

        self.register_button = tk.Button(self.root, text="Register", command=self.register, width=15, font=10, highlightthickness=2, background='pink', fg='maroon', bd=3)

        self.window_width = self.screen_width
        self.window_height = self.screen_height

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            if firebase_connection.create_owner_login_id(username, password):
                self.root.destroy()
                Owner_Dashboard.OwnerDashboardClass().run()
            else:
                messagebox.showerror('Signup failed!', 'It looks somthing wrong try again!')

    def place_widgets(self):
        label_x = self.window_width // 2
        label_y = self.window_height // 2
        entry_x = label_x + 100  # Adjust as needed
        entry_y = label_y
        button_x = label_x
        button_y = label_y + 100  # Adjust as needed

        self.username_label.place(x=label_x + 30, y=label_y - 80, anchor="center")
        self.username_entry.place(x=entry_x + 20, y=entry_y - 50, anchor="center")
        self.password_label.place(x=label_x + 30, y=label_y - 15, anchor="center")
        self.password_entry.place(x=entry_x + 20, y=entry_y + 15, anchor="center")
        self.confirm_password_label.place(x=label_x + 67, y=label_y + 50, anchor="center")
        self.confirm_password_entry.place(x=entry_x + 19, y=entry_y + 80, anchor="center")
        self.register_button.place(x=button_x + 173, y=button_y + 25, anchor="center")

    def run(self):
        self.root.mainloop()


# Create an instance of the SignupClass and start the application
# signup_page = SignupClass()
# signup_page.place_widgets()
# signup_page.run()
