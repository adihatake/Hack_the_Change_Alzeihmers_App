import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.title("Test")
root.geometry("400x550")

my_image = ctk.CTkImage(light_image=Image.open("Practice/Calgary.jpg"),
                        dark_image = Image.open("Practice/Calgary.jpg"),
                        size=(180,250))
my_label = ctk.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)

root.mainloop()