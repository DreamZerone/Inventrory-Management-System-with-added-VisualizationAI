import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import test2


def manage_membership():
    t = test2.test1()
    t.start()


class test1:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sign Up")
        self.root.state("zoom")
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        self.image = Image.open("risen-wang-20jX9b35r_M-unsplash.jpg")
        self.image = self.image.resize((screen_width, screen_height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(relwidth=1, relheight=1)

        membership_button = tk.Button(self.root, text="Buy Memberships", command=manage_membership, background='pink', bd=20)
        membership_button.place(x=700, y=100)

    def start(self):
        self.root.mainloop()

t1 = test1()
t1.start()
