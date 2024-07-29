import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
import login
import User_Signup
import Owner_Signup


class LandingPageClass:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sign Up")
        self.root.state("zoom")
        icon_path = 'gymIcon.ico'
        self.root.iconbitmap(icon_path)

        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        self.photo = Image.open("risen-wang-20jX9b35r_M-unsplash.jpg")
        self.photo = self.photo.resize((screen_width, screen_height))
        self.photo = ImageTk.PhotoImage(self.photo)

        self.bg_label = tk.Label(self.root, image=self.photo)
        self.bg_label.place(relwidth=1, relheight=1)

        def icon_r():
            messagebox.showinfo("Secured!", "Verified mark thank you!")

        def clicked_login():
            self.root.destroy()
            # self.root.withdraw()
            login.LoginClass().start()

        def clicked_owner_signup():
            self.root.destroy()
            signup_page = Owner_Signup.SignupClass()
            signup_page.place_widgets()
            signup_page.run()

        def clicked_user_signup():
            self.root.destroy()
            signup_page = User_Signup.SignupClass()
            signup_page.place_widgets()
            signup_page.run()

        txt = 'Welcome to MyGym'
        lbl = tk.Label(self.bg_label, font='Bell 36 bold', width=len(txt), background='black', foreground='white')
        login_button = tk.Button(self.bg_label, command=clicked_login, text="Login", background='pink')

        original_icon = tk.Button(self.bg_label, command=icon_r, text="R", background='red')
        lbl.place(x=10, y=10)
        login_button.place(x=1200, y=20)
        original_icon.place(x=865, y=10)
        login_button.config(height=2, width=7)
        lbl.pack(pady=5)

        def animate_label(text, n=0):
            if n < len(text) - 1:
                lbl.after(100, animate_label, text, n + 1)
            lbl['text'] = text[:n + 1]

        self.bg_label.after(1000, animate_label, txt)

        canvas = tk.Canvas(self.bg_label)
        canvas.pack()
        canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW, fill='white', font=5)

        welcome_gym_owner = "'' Welcome to the fitness haven you've been searching for! \n" \
                            " At MyGym, we're committed to providing you \n" \
                            " with the best fitness experience possible. Whether you're \n" \
                            " a seasoned fitness enthusiast or just starting your fitness \n" \
                            " journey, our state-of-the-art equipment, expert trainers, and \n" \
                            " a supportive community are here to help you reach your goals.\n" \
                            " Join us today and embark on a fitness adventure like no other. ''\n\n\n" \
                            " '' Your dream body and a healthier lifestyle are just a workout away!\n" \
                            " Are you ready to revolutionize your gym management experience? \n" \
                            " Look no further! We understand the challenges you face in running \n" \
                            " a successful fitness facility, from member management to equipment\n" \
                            " maintenance and everything in between. Our gym management solutions\n" \
                            " are designed to make your life easier, allowing you to focus on \n" \
                            " what you do best - helping your members achieve their fitness goals.\n" \
                            " Join us today and take the first step towards an efficient, streamlined,\n" \
                            " and prosperous gym operation. ''"

        addDur = 10
        delay = 0
        for i in range(len(welcome_gym_owner) + 1):
            s = welcome_gym_owner[:i]
            update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
            canvas.place(x=100, y=100)
            canvas.configure(background='gray')
            canvas.config(height=450, width=650)
            canvas.after(delay, update_text)
            delay += addDur

        owner = tk.Button(self.root, command=clicked_owner_signup, text="Make your own inventory", width=15, font=10,
                          highlightthickness=2,
                          background='pink',
                          fg='maroon', bd=5)
        user = tk.Button(self.root, command=clicked_user_signup, text="Book your first Appointment", width=15, font=10,
                         highlightthickness=2,
                         background='pink',
                         fg='maroon', bd=5)

        owner.config(height=2, width=30)
        user.config(height=2, width=30)

        owner.place(x=900, y=350)
        user.place(x=900, y=450)

    def run(self):
        self.root.mainloop()


# Create an instance of the LandingPageClass and start the application
landing_page = LandingPageClass()
landing_page.run()
