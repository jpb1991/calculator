import tkinter as tk
import numpy as np
import scipy.special as sp

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FNBubbles420 Org Calculator")
        self.geometry("450x600")  # Adjusted for better proportion
        
        self.init_ui()
        
    def init_ui(self):
        self.create_entry()
        self.create_buttons()

    def create_entry(self):
        entry_font = ("Verdana", 24, "bold")  # More modern font
        self.entry = tk.Entry(self, font=entry_font, borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky="nsew")

    def create_buttons(self):
        pale_blue = "#D7E3FC"
        button_params = {
            'font': ("Verdana", 14),  # Unified font style
            'bg': pale_blue,
            'width': 8,
            'height': 2
        }
        buttons = [
