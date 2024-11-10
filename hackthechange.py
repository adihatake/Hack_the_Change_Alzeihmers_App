import customtkinter as ctk
import tkinter as kt
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class FacialFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="springgreen3", corner_radius=10, height=560)        
        
        # Facial frame
        self.grid_columnconfigure(0, weight=1)
        self.exit = False


        # Displaying memory photo
        family_image = Image.open("Photos\FamilyPhoto.jpg")

        self.family_image = ctk.CTkImage(dark_image=family_image,
            size=(453, (453 / family_image.size[0]) * family_image.size[1]))
        
        self.image_label = ctk.CTkLabel(self, text="", image=self.family_image, )
        self.image_label.grid(row=3,column=0 , padx=10, pady=(0,20), sticky="n", columnspan = 2)


        # Context for memory
        self.memory_info = kt.Label(self, text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
                                         wraplength=750, font=('Arial', 18))
        self.memory_info.grid(row=2, column=0, padx=10, pady=5, sticky="ew", columnspan = 2)


        # Text label for meeting person alert
        self.meeting_label = ctk.CTkLabel(self, text="You are meeting [NAME]\nThey are your [RELATIONSHIP]", fg_color="navy", corner_radius=6,
                                         font=('Arial', 14), text_color='White', wraplength=360)
        self.meeting_label.grid(row=0, column=0, padx=10, pady= (10,5), sticky = "ew")


        # Exit Button
        self.exit_bttn = ctk.CTkButton(self, text="X", fg_color="Black", corner_radius=8, 
                                       font=('Arial', 10), text_color="White", command= self.ExitFacialFrame, width=30, 
                                       hover_color="Red")
        self.exit_bttn.grid(row=0, column=1, padx=10, pady=10, sticky= "e")


    # Close facial recognition alert
    def ExitFacialFrame(self):
        if self.exit == False:
            self.exit_bttn._fg_color = "Red"
            self.exit = True
        else:
            self.grid_forget()
            self.exit = False
        


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main frame
        self.title("MemoryHub")
        self.geometry("453x806")
        self.grid_columnconfigure(0, weight=1)


        # Background image
        background_image = Image.open("Photos\City.jpg")

        self.background_image = ctk.CTkImage(dark_image=background_image,
            size=((806 / background_image.size[1]) * background_image.size[0], 806))
        
        self.background_label = ctk.CTkLabel(self, text="", image= self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Facial recognition alert frame
        self.facial_recog_frame = FacialFrame(self)

        # Edit information button
        edit_icon = Image.open("Photos\EditInfoIcon.png")

        self.edit_icon = ctk.CTkImage(dark_image=edit_icon,
            size = (75,75))

        self.edit_info_bttn = ctk.CTkButton(self, image= self.edit_icon, text="", fg_color="Yellow",
            height=100, width=100, corner_radius=10, hover_color="yellow2")
        self.edit_info_bttn.place(x=333, y=686)

        # Start checking for face
        self.read_from_file()

        # Background context text
        self.background_context = ctk.CTkLabel(self, text="Background is a picture of [EVENT] on [DATE] with [NAME(S)]",
                wraplength=420, fg_color= "RoyalBlue4", font=('Arial', 15))
        self.background_context.grid(row=0, column=0, columnspan=2, sticky="we", padx=10, pady=(10,0))

    # FIX THIS
    def read_from_file(self):
        # Function to read from a .txt file and update the label
        try:
            with open("memory.txt", "r") as file:
                content = file.read()

                if content == "adi" and self.facial_recog_frame.winfo_ismapped() == False:
                    print("Person Alert!")
                    self.facial_recog_frame = FacialFrame(self)
                    self.facial_recog_frame.grid(row=1, column=0, padx=10, pady=(20,10), sticky="nsew")
        except FileNotFoundError:
            print("File not found")

        self.after(2000, self.read_from_file)

app = App()
app.mainloop()
