import customtkinter as ctk

class MyRadioButtonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        # Checkboxes
        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable = self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()
    
    def set(self,value):
        self.variable.set(value)
    

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        # Checkboxes
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []

        # 1 = checked
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))

        return checked_checkboxes


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame
        self.checkbox_frame_1 = MyCheckboxFrame(self, "Values", values=["Value 1", "Value 2", "Value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.radiobutton_frame = MyRadioButtonFrame(self, "Options", values=["Option 1", "Option 2"])
        self.radiobutton_frame.grid(row=0, column=1, padx=(0,10), pady=(10,0), sticky="nsew")

        # Buttons
        self.button = ctk.CTkButton(self, text = "my button", command = self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan = 2)

    def button_callback(self):
        print("checkbox_frame_1:", self.checkbox_frame_1.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())

app = App()
app.mainloop()
