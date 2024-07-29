import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class Test1:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test1")

        # Load and display an image using Pillow and PhotoImage
        image_path = "dashboardbackgroundImage.jpg"  # Replace with the path to your image file

        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.bg_label = tk.Label(self.root, image=photo)
            self.bg_label.pack()

            # Run the Tkinter main loop
            self.root.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    t = Test1()
