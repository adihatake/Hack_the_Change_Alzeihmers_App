import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class FacialFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        family_image = Image.open("Photos\FamilyPhoto.jpg")

        self.family_image = ctk.CTkImage(dark_image=family_image,
            size=(453, (453 / family_image.size[0]) * family_image.size[1]))
        
        self.image_label = ctk.CTkLabel(self, text="", image=self.family_image)
        self.image_label.grid(row=1, column=0, padx=10, pady=(0,20), sticky="n")

        self.memory_label = ctk.CTkLabel(self, text="This is xyz memory from xyz date with xyz person", fg_color="Cyan", corner_radius=6,
                                         font=('Arial', 18), text_color='Purple')
        self.memory_label.grid(row=0, column=0, padx=10, pady=20)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MemoryHub")
        self.geometry("453x806")
        self.grid_columnconfigure(0, weight=1)

        background_image = Image.open("Photos\City.jpg")

        self.background_image = ctk.CTkImage(dark_image=background_image,
            size=((806 / background_image.size[1]) * background_image.size[0], 806))
        
        self.background_label = ctk.CTkLabel(self, text="", image= self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.facial_recog_frame = FacialFrame(self)
        self.facial_recog_frame.grid(row=0, column=0, padx=10, pady=(20,10), sticky="nsew")

app = App()
app.mainloop()