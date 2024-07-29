import json
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes

import Owner_Dashboard
import firebase_connection


def manage_appointment():
    root = Tk()
    root.state('zoom')
    root.title('appointments')
    root.configure(bg='lightblue')
    icon_path = 'gymIcon.ico'
    root.iconbitmap(icon_path)
    
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    image = Image.open("jelmer-assink-gzeTjGu3b_k-unsplash.jpg")
    image = image.resize((screen_width, screen_height))
    image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=image)
    bg_label.place(relwidth=1, relheight=1)

    sb = Scrollbar(bg_label, width=50, bg='black')
    sb.pack(side=RIGHT, fill=Y)

    def prevPage():
        root.destroy()
        Owner_Dashboard.OwnerDashboardClass()

    prev_button = tk.Button(root, command=prevPage, text=" < ", background='pink')
    prev_button.place(x=10, y=15)

    mylist = Listbox(bg_label, yscrollcommand=sb.set, height=25, width=60, background='gray', fg='white', border=20, font=10)

    mylist.insert(END, "!!! APPOINTMENTS LIST !!!")

    json_data = firebase_connection.sending_appointments_data()
    # Converting JSON to a string with line-separated data
    json_string = json.dumps(json_data, indent=4)  # Converting to a formatted JSON string
    lines = json_string.splitlines()  # Splitting the string into lines

    if lines:
        for line in lines:
            mylist.insert(END, line)
    else:
        messagebox.showerror('error', 'an error occurred while loading data try to re-open!')

    mylist.pack(side=RIGHT)
    sb.config(command=mylist.yview)
    mainloop()

#
# manage_appointment()
