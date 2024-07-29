import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
import buymembership
import book_appointments
import login
import userInventoryAndSupplies


class userDashboardClass:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.state('zoom')
        self.root.title("User Dashboard")
        icon_path = 'gymIcon.ico'
        self.root.iconbitmap(icon_path)

        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        image = Image.open("dashboardbackgroundImage.jpg")
        image = image.resize((screen_width, screen_height))
        self.photo = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(relwidth=1, relheight=1)

        def manage_membership():
            self.root.destroy()
            buymembership.MembershipClass(username).run()

        def manage_appointment():
            self.root.destroy()
            book_appointments.book_appointment_class(username).run()

        def manage_inventory():
            self.root.destroy()
            userInventoryAndSupplies.inventory(username)

        def prevPage():
            self.root.destroy()
            login.LoginClass()

        self.prev_button = tk.Button(self.root, command=prevPage, text=" < ", background='pink')
        self.prev_button.place(x=10, y=15)

        membership_button = tk.Button(self.root, text="Buy Memberships", command=manage_membership,
                                      background='pink', bd=20)
        classes_button = tk.Button(self.root, text="Book Appointments", command=manage_appointment, background='Gray',
                                   bd=20)
        integrations_button = tk.Button(self.root, text="Available equipment\n and Supplies",
                                        command=manage_inventory, background='Teal', bd=20)
        profile = tk.Label(self.root, text="Hello, Welcome " + username, font=10, background="#f4f2f5", foreground='black', bd=25)

        membership_button.grid(row=0, column=0, padx=10, pady=10)
        classes_button.grid(row=0, column=2, padx=10, pady=10)
        integrations_button.grid(row=1, column=2, padx=10, pady=10)

        membership_button.place(x=700, y=100)
        classes_button.place(x=700, y=300)
        integrations_button.place(x=700, y=500)
        profile.place(x=20, y=45)

        membership_button.config(height=5, width=20)
        classes_button.config(height=5, width=20)
        integrations_button.config(height=5, width=20)
        profile.config(height=1, width=20)

    def run(self):
        self.root.mainloop()


# Create an instance of the OwnerDashboardClass and start the dashboard
# owner_dashboard = userDashboardClass('sita')
# owner_dashboard.run()
