# import customtkinter as tk
#
# from register_view import RegisterView
#
#
# class LoginView:
#     def __init__(self, master):
#         self.master = master
#         for widget in self.master.winfo_children():
#             widget.destroy()
#
#         login_label = tk.CTkLabel(master=self.master, text="Login System", corner_radius=10, font=("Roboto", 30))
#         login_label.pack(pady=12, padx=10)
#
#         username_entry = tk.CTkEntry(master=self.master, placeholder_text="Username", placeholder_text_color="grey",
#                              font=("Roboto", 14), height=36, width=150)
#         username_entry.pack(pady=8, padx=10)
#
#         password_entry = tk.CTkEntry(master=self.master, placeholder_text="Password", placeholder_text_color="grey",
#                              font=("Roboto", 14), height=36, width=150)
#         password_entry.pack(pady=8, padx=10)
#
#         login_button = tk.CTkButton(master=self.master, text="Login", command=lambda: self.login(), font=("Roboto", 15))
#         login_button.pack(pady=(12, 3), padx=5)
#
#         no_account_label = tk.CTkLabel(master=self.master, text="Don't have an account?", corner_radius=10)
#         no_account_label.pack(pady=(12, 0))
#
#         sing_up_label = tk.CTkLabel(master=self.master, text="Sign up here!", corner_radius=10, font=("Roboto", 17),
#                              text_color="cyan",
#                              text_color_disabled="yellow")
#         sing_up_label.pack()
#         sing_up_label.bind(sequence="<Button-1>", command=lambda event: self.register())
#
#     def open_new_window(self):
#         for widget in self.master.winfo_children():
#             widget.destroy()
#
#         label = tk.CTkLabel(master=self.master, text="New Window", corner_radius=10, font=("Roboto", 30))
#         label.pack(pady=12, padx=10)
#
#         button = tk.CTkButton(master=self.master, text="Back", command=lambda: self.__init__(self.master), font=("Roboto", 15))
#         button.pack(pady=(12, 3), padx=5)
#
#
#
#     def login(self):
#         print("Login")
#         self.open_new_window()
#
#     def register(self):
#         print("Register")
#         RegisterView(master=self.master)
#
#
#
