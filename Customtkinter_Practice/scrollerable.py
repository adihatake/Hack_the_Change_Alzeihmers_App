import customtkinter as ctk

class ScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

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
        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_frame = ScrollableCheckboxFrame(self, "Values", values=values)
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

        # Buttons
        self.button = ctk.CTkButton(self, text = "my button", command = self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan = 2)

    def button_callback(self):
        print("checkbox_frame_1:", self.scrollable_frame.get())

app = App()
app.mainloop()