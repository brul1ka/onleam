import customtkinter as ctk
from main_window import OnleamApp


def main():
    ctk.set_appearance_mode("dark")
    app = OnleamApp()
    app.mainloop()


if __name__ == "__main__":
    main()
