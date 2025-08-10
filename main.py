# main.py
import customtkinter as ctk
import webbrowser
from Pastrix import PastrixTyper
from PIL import Image
import os
import sys
from datetime import datetime

# --- Definitive Path Fix ---
# Get absolute path to resource, works for dev and for PyInstaller
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

__version__ = "FINAL"

class App(ctk.CTk):
    def __init__(self, typer):
        super().__init__()

        self.typer = typer
        
        # ---- Window Setup ----
        self.title("PASTRIX")
        self.geometry("500x440")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        icon_path = resource_path(os.path.join("assets", "icon.ico"))
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        # ---- Widgets ----
        self.title_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.title_frame.pack(pady=(15, 5))
        
        title_font = ctk.CTkFont(size=40, weight="bold")
        red_color = "#db4437"
        
        ctk.CTkLabel(self.title_frame, text="P", font=title_font).pack(side="left")
        ctk.CTkLabel(self.title_frame, text="as", font=title_font, text_color=red_color).pack(side="left")
        ctk.CTkLabel(self.title_frame, text="t", font=title_font).pack(side="left")
        ctk.CTkLabel(self.title_frame, text="r", font=title_font, text_color=red_color).pack(side="left")
        ctk.CTkLabel(self.title_frame, text="ix", font=title_font).pack(side="left")

        self.instruction_label = ctk.CTkLabel(self, text="Press shortcut key to paste from clipboard", font=ctk.CTkFont(size=12))
        self.instruction_label.pack(pady=(0, 10))

        # --- Options Frame ---
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=5, padx=20, fill="x")

        self.mode_label = ctk.CTkLabel(self.options_frame, text="Mode:")
        self.mode_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.mode_var = ctk.StringVar(value=self.typer.mode)
        for i, mode in enumerate(self.typer.modes):
            radio = ctk.CTkRadioButton(self.options_frame, text=mode.replace("-", " ").title(), variable=self.mode_var, value=mode, command=lambda m=mode: self.typer.set_mode(m))
            radio.grid(row=0, column=i+1, padx=10, pady=10, sticky="w")

        self.shortcut_label = ctk.CTkLabel(self.options_frame, text="Shortcut Key:")
        self.shortcut_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.shortcut_var = ctk.StringVar(value=self.typer.shortcut_key)
        for i, key in enumerate(self.typer.shortcut_keys):
            radio = ctk.CTkRadioButton(self.options_frame, text=key, variable=self.shortcut_var, value=key, command=lambda k=key: self.typer.set_shortcut_key(k))
            radio.grid(row=1, column=i+1, padx=10, pady=10, sticky="w")
        
        # --- Switches Frame ---
        self.switch_frame = ctk.CTkFrame(self)
        self.switch_frame.pack(pady=10, padx=20, fill="x")
        self.switch_frame.grid_columnconfigure(1, weight=1)

        self.line_break_var = ctk.BooleanVar(value=self.typer.line_break)
        self.line_break_label = ctk.CTkLabel(self.switch_frame, text="Line Break")
        self.line_break_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.line_break_switch = ctk.CTkSwitch(self.switch_frame, text="", variable=self.line_break_var, command=lambda: self.typer.set_line_break(self.line_break_var.get()))
        self.line_break_switch.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.remove_everything_var = ctk.BooleanVar(value=self.typer.remove_everything)
        self.remove_everything_label = ctk.CTkLabel(self.switch_frame, text="Clear Field Before Pasting")
        self.remove_everything_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.remove_everything_switch = ctk.CTkSwitch(self.switch_frame, text="", variable=self.remove_everything_var, command=lambda: self.typer.set_remove_everything(self.remove_everything_var.get()))
        self.remove_everything_switch.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        
        self.remove_brackets_var = ctk.BooleanVar(value=self.typer.remove_auto_brackets)
        self.remove_brackets_label = ctk.CTkLabel(self.switch_frame, text="Remove Auto Brackets")
        self.remove_brackets_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.remove_brackets_switch = ctk.CTkSwitch(self.switch_frame, text="", variable=self.remove_brackets_var, command=lambda: self.typer.set_remove_auto_brackets(self.remove_brackets_var.get()))
        self.remove_brackets_switch.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        
        # --- Control Button ---
        self.status_var = ctk.StringVar(value="START")
        self.toggle_button = ctk.CTkButton(self, textvariable=self.status_var, font=ctk.CTkFont(weight="bold"), command=self.toggle_service)
        self.toggle_button.pack(pady=15, ipady=5)

        # ---- FOOTER SECTION ----
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.pack(side="bottom", fill="x", pady=(0, 5))

        copyright_text = f"© {datetime.now().year} Akash Singh Rathaur  |  v{__version__}"
        self.copyright_label = ctk.CTkLabel(self.footer_frame, text=copyright_text, font=ctk.CTkFont(size=10), text_color="gray")
        self.copyright_label.pack(side="left", padx=15)

        self.socials_frame = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.socials_frame.pack(side="right", padx=10)
        
        social_media_links = {
            "github": "https://github.com/akashsrathaur",
            "linkedin": "https://www.linkedin.com/in/akashsrathaur/",
            "instagram": "https://www.instagram.com/akashsrathaur/"
        }

        for name, url in social_media_links.items():
            image_path = resource_path(os.path.join("assets", f"{name}.png"))
            if os.path.exists(image_path):
                pil_image = Image.open(image_path).convert("RGBA")
                resized_image = pil_image.resize((20, 20), Image.Resampling.LANCZOS)
                ctk_image = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(20, 20))
                
                button = ctk.CTkButton(
                    self.socials_frame, image=ctk_image, text="", width=20, height=20,
                    fg_color="transparent", hover_color="#555555",
                    command=lambda u=url: webbrowser.open_new(u)
                )
                button.image = ctk_image
                button.pack(side="left", padx=4)

    def toggle_service(self):
        if self.status_var.get() == "START":
            self.typer.start()
            self.status_var.set("STOP")
            self.toggle_button.configure(fg_color="#db4437", hover_color="#c53d2e")
        else:
            self.typer.stop()
            self.status_var.set("START")
            self.toggle_button.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"], hover_color=ctk.ThemeManager.theme["CTkButton"]["hover_color"])

if __name__ == "__main__":
    try:
        pastrix_typer = PastrixTyper(mode="ace-editor")
        app = App(typer=pastrix_typer)
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("PASTRIX has been shut down.")