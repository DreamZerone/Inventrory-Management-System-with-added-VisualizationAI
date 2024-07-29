import tkinter as tk
from tkinter import messagebox

import pandas as pd
from PIL import Image, ImageTk
import ctypes

import OwnerInventryAndSupplies
import firebase_connection
import login
import manage_membership_data
import manage_appointments_data
import member_profile
import VisualizationAI


def manage_billing():
    messagebox.showinfo("Manage Billing", " manage billing")


class OwnerDashboardClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state('zoom')
        self.root.title("Owner Dashboard")
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

        def prevPage():
            self.root.destroy()
            login.LoginClass()

        self.prev_button = tk.Button(self.root, command=prevPage, text=" < ", background='pink')
        self.prev_button.place(x=10, y=15)

        def manage_membership():
            self.root.destroy()
            manage_membership_data.manage_membership()

        def manage_appointments():
            self.root.destroy()
            manage_appointments_data.manage_appointment()

        def manage_Profile():
            self.root.destroy()
            member_profile.manage_member_profile()

        def manage_inventory():
            self.root.destroy()
            OwnerInventryAndSupplies.inventory()

        def reportsAndAnalytics():
            self.root.destroy()
            VisualizationAI.Visualization()

        def downloadMembershipDataset():
            data = firebase_connection.download_membership_data_dataset()
            # Converting the data to a Pandas DataFrame
            df = pd.DataFrame.from_dict(data, orient='index')
            # Saving the DataFrame as a CSV file
            df.to_csv('downloadMembershipData.csv', index=False)

        membership_dataset_download_button = tk.Button(self.root, text="Download Membership Dataset ", command=downloadMembershipDataset,
                                      background='green', bd=5)
        membership_dataset_download_button.place(x=1050, y=40)

        def downloadAppointmentDataset():
            data = firebase_connection.download_appointment_data_dataset()
            # Converting the data to a Pandas DataFrame
            df = pd.DataFrame.from_dict(data, orient='index')
            # Saving the DataFrame as a CSV file
            df.to_csv('downloadAppointmentData.csv', index=False)

        Appointment_dataset_download_button = tk.Button(self.root, text="Download Appointment Dataset", command=downloadAppointmentDataset,
                                      background='green', bd=5)
        Appointment_dataset_download_button.place(x=1050, y=80)

        membership_button = tk.Button(self.root, text="Manage Memberships", command=manage_membership,
                                      background='pink', bd=20)
        billing_button = tk.Button(self.root, text="Manage Billing", command=manage_billing, background='Cyan',
                                   bd=20)
        classes_button = tk.Button(self.root, text="Appointments", command=manage_appointments, background='Gray',
                                   bd=20)
        communication_button = tk.Button(self.root, text="Reports and Analytics", command=reportsAndAnalytics,
                                         background='Crimson', bd=20)
        feedback_button = tk.Button(self.root, text="Member Profile", command=manage_Profile, background='pink',
                                    bd=20)
        integrations_button = tk.Button(self.root, text="Inventory and Supplies", command=manage_inventory,
                                        background='Teal', bd=20)

        membership_button.grid(row=0, column=0, padx=10, pady=10)
        billing_button.grid(row=0, column=1, padx=10, pady=10)
        classes_button.grid(row=0, column=2, padx=10, pady=10)
        communication_button.grid(row=1, column=0, padx=10, pady=10)
        feedback_button.grid(row=1, column=1, padx=10, pady=10)
        integrations_button.grid(row=1, column=2, padx=10, pady=10)

        membership_button.place(x=250, y=200)
        billing_button.place(x=550, y=200)
        classes_button.place(x=850, y=200)
        communication_button.place(x=250, y=400)
        feedback_button.place(x=550, y=400)
        integrations_button.place(x=850, y=400)

        membership_button.config(height=5, width=20)
        billing_button.config(height=5, width=20)
        classes_button.config(height=5, width=20)
        communication_button.config(height=5, width=20)
        feedback_button.config(height=5, width=20)
        integrations_button.config(height=5, width=20)

    def run(self):
        self.root.mainloop()


# Create an instance of the OwnerDashboardClass and start the dashboard
# owner_dashboard = OwnerDashboardClass()
# owner_dashboard.run()
