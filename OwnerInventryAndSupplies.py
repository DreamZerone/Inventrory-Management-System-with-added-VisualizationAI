import json
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes

import Owner_Dashboard
import firebase_connection


def inventory():
    root = Tk()
    root.state('zoom')
    root.title('membership')
    root.configure(bg='lightblue')

    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    image = Image.open("jelmer-assink-gzeTjGu3b_k-unsplash.jpg")
    image = image.resize((screen_width, screen_height))
    image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=image)
    bg_label.place(relwidth=1, relheight=1)

    def prevPage():
        root.destroy()
        Owner_Dashboard.OwnerDashboardClass()

    sb = Scrollbar(bg_label, width=50, bg='black')
    sb.pack(side=LEFT, fill=Y)

    prev_button = tk.Button(root, command=prevPage, text=" < ", background='pink')
    prev_button.place(x=10, y=15)

    mylist = Listbox(bg_label, yscrollcommand=sb.set, height=25, width=60, background='gray', fg='white', border=20,
                     font=10)

    mylist.insert(END, "!!! INVENTORY AND SUPPLIES !!!")

    """json_data = {
        "Youth (10-18 years)": {
            "Treadmill": "Cardiovascular exercises",
            "Dumbbells": "Strength training",
            "Jump Rope": "Cardio and agility",
            "Resistance Bands": "Full-body workouts",
            "Stationary Bike": "Low-impact cardio",
            "Swimming": "Full-body workout and endurance",
            "Boxing Bag": "Boxing and coordination",
            "Climbing Wall": "Strength and endurance",
            "Soccer Ball": "Soccer and team sports",
            "Basketball Hoop": "Basketball and shooting practice",
        },
        "Adults (19-50 years)": {
            "Elliptical Trainer": "Low-impact cardio",
            "Barbell": "Weight lifting and strength training",
            "Yoga Mat": "Flexibility and relaxation",
            "Exercise Ball": "Core workouts and balance",
            "Rowing Machine": "Total body workout",
            "Pilates Reformer": "Core strength and flexibility",
            "Kettle bell": "Functional training and power",
            "Spin Bike": "High-intensity interval training (HIIT)",
            "TRX Suspension Trainer": "Full-body resistance training",
            "Boxing Gloves": "Boxing and self-defense",
        },
        "Seniors (50+ years)": {
            "Recumbent Bike": "Low-impact cardio",
            "Light Dumbbells": "Strength maintenance",
            "Tai Chi Ball": "Balance and coordination",
            "Stretch Bands": "Gentle stretching and flexibility",
            "Aqua Aerobics": "Low-impact water exercise",
            "Tai Chi": "Balance, flexibility, and relaxation",
            "Walking Stick": "Gentle walking and balance",
            "Resistance Chair": "Strength and stability exercises",
            "Theraband": "Rehabilitation and flexibility",
            "Bowling Ball": "Bowling and social activity",
        }
    }"""

    json_data = firebase_connection.getInventoryData()

    def loadData(data):
        if data:
            row = 0
            for age_group, exercises in data.items():
                mylist.insert(END, '')
                icon = "\u26B4"
                mylist.insert(END, '\t\t\t\t\t\t\t\t\t\t\t\t' + icon + ' ' + age_group)
                mylist.insert(END, '')
                row += 1

                for equipment, exercise_type in exercises.items():
                    icon = "\u26B6"
                    mylist.insert(END, icon + ' ' + equipment + '                  -' + exercise_type)
                    row += 1
        else:
            messagebox.showerror('error', 'an error occurred while loading data try to re-open!')

    loadData(json_data)

    add_data_entry = tk.Entry(root, width=25, font=10, highlightthickness=2, highlightbackground='black', bd=3)
    remove_data_entry = tk.Entry(root, width=25, font=10, highlightthickness=2, highlightbackground='black', bd=3)

    def setData():
        messagebox.showerror('warning?', 'Under maintenance!')

    def deleteData():
        if firebase_connection.deleteInventoryData(remove_data_entry.get()):
            messagebox.showinfo('success', 'Successfully deleted refresh the page!')
            mylist.delete(0, tk.END)
            data = firebase_connection.getInventoryData()
            loadData(data)

    add_data_button = tk.Button(root, text="add", command=setData, background='green', foreground='white', height=1,
                                width=6)
    remove_data_button = tk.Button(root, text="remove", command=deleteData, background='red', foreground='white',
                                   height=1, width=6)

    add_data_entry.place(x=850, y=400)
    add_data_button.place(x=1150, y=408)
    remove_data_entry.place(x=850, y=450)
    remove_data_button.place(x=1150, y=458)

    mylist.pack(side=LEFT)
    sb.config(command=mylist.yview)
    mainloop()


# inventory()
