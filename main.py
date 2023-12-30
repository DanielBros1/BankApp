import customtkinter as tk

from authentication_view import BaseView
from authentication_view import LoginView


class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.frame = tk.CTkFrame(master=self.master)
        self.frame.pack(padx=15, pady=20, fill=tk.BOTH, expand=True)

        # Initial content
        LoginView(master=self.frame)

        # Initial appearance and theme
        self.set_initial_appearance_and_theme()

    @staticmethod
    def set_initial_appearance_and_theme():
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")


if __name__ == "__main__":
    root = tk.CTk()
    app = MyApp(root)
    root.mainloop()
