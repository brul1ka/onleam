import customtkinter as ctk


class OnleamApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Onleam")
        self.geometry("900x500")

        # Настраиваем сетку (grid) 1x2 (боковая панель и основная часть)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. Боковая панель
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(
            self.navigation_frame,
            text="ONLEAM",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(
            self.navigation_frame,
            text="Search",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
        )
        self.home_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        self.fav_button = ctk.CTkButton(
            self.navigation_frame,
            text="Favorites",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
        )
        self.fav_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.search_entry = ctk.CTkEntry(
            self.main_frame, placeholder_text="Enter game name...", width=400, height=40
        )
        self.search_entry.pack(pady=(20, 10))

        self.search_btn = ctk.CTkButton(self.main_frame, text="Check Online", width=150)
        self.search_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.main_frame, text="Waiting for input...", font=("Arial", 12)
        )
        self.status_label.pack(pady=20)


if __name__ == "__main__":
    app = OnleamApp()
    app.mainloop()
