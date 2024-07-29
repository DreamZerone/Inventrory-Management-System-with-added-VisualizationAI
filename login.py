import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
import Owner_Dashboard
import landingPage
import user_dashboard
import firebase_connection


class LoginClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.state("zoom")
        self.root.configure(background='lightblue')
        icon_path = 'gymIcon.ico'
        self.root.iconbitmap(icon_path)

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

        # creating animative switch to ask user of owner login

        self.canvas = tk.Canvas(self.root, width=100, height=20, bg="white")
        self.canvas.place(x=800, y=288)
        self.switch_button = self.canvas.create_rectangle(0, 20, 50, 0,fill="green", outline="black")

        self.left_label = tk.Label(self.root, text="ADMIN\t\t", font=("Helvetica", 7), background='black', foreground='red')
        self.left_label.place(x=802, y=270)
        self.right_label = tk.Label(self.root, text="USER", font=("Helvetica", 7), background='black', foreground='red')
        self.right_label.place(x=870, y=270)

        self.switch_state = False  # Represents the state of the slide switch

        self.canvas.bind("<Button-1>", self.toggle_switch)

    # getting the switch value for knowing that who is logging____
    switch_data = True

    def toggle_switch(self, event):
        if self.switch_state:
            self.slide_to_left()
        else:
            self.slide_to_right()

    def slide_to_left(self):
        self.switch_data = True
        if self.switch_state:
            for i in range(40):
                self.canvas.move(self.switch_button, -1, 0)
                self.root.update()
                self.root.after(1)
            self.switch_state = False

    def slide_to_right(self):
        self.switch_data = False
        if not self.switch_state:
            for i in range(50):
                self.canvas.move(self.switch_button, 1, 0)
                self.root.update()
                self.root.after(1)
            self.switch_state = True

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if self.switch_data:
                if firebase_connection.checking_owner_login_credential(username, password):
                    self.root.destroy()
                    Owner_Dashboard.OwnerDashboardClass().run()
                else:
                    messagebox.showerror('Not found', 'username/password is invalid!')

            else:
                if firebase_connection.checking_user_login_credential(username, password):
                    self.root.destroy()
                    user_dashboard.userDashboardClass(username).run()
                else:
                    messagebox.showerror('Not found', 'username/password is invalid!')

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
