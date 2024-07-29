import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes


class LoginClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
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

        self.username_label = tk.Label(self.root, text="Username:", font=10, background='gray', foreground='white',
                                       bd=35)
        self.password_label = tk.Label(self.root, text="Password:", font=10, background='gray', foreground='white',
                                       bd=35)

        self.username_entry = tk.Entry(self.root, width=25, font=10, highlightthickness=2, highlightbackground='black',
                                       bd=3)
        self.password_entry = tk.Entry(self.root, show="*", width=25, font=10, highlightthickness=2,
                                       highlightbackground='black', bd=3)

        self.register_button = tk.Button(self.root, text="Login", command=self.register, width=15, font=10,
                                         highlightthickness=2, background='pink', fg='maroon', bd=3)

        self.center_widgets(self.screen_width, self.screen_height)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showinfo("Success", "Registration successful!")

    def center_widgets(self, window_width, window_height):
        label_x = window_width // 2
        label_y = window_height // 2
        entry_x = window_width // 2 + 100
        entry_y = window_height // 2
        button_x = window_width // 2
        button_y = window_height // 2 + 100

        self.username_label.place(x=label_x + 30, y=label_y - 50, anchor="center")
        self.username_entry.place(x=entry_x + 20, y=entry_y - 20, anchor="center")
        self.password_label.place(x=label_x + 30, y=label_y + 15, anchor="center")
        self.password_entry.place(x=entry_x + 20, y=entry_y + 45, anchor="center")
        self.register_button.place(x=button_x + 173, y=button_y - 10, anchor="center")

    def start(self):
        self.root.mainloop()

# Create an instance of the LoginClass and start the application
# login_app = LoginClass()
# login_app.start()
