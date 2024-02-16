import tkinter as tk_standard
import customtkinter as tk


class SettingsFrame:
    def __init__(self, master, user_info):
        self.master = master
        self.user_info = user_info
        self.my_colors = {
            "dark_grey_color": "#2B2B2B",
            "very_dark_grey_color": "#1E1E1E",
            "some_dark_grey_color": "#4A4A4A",
            "light_grey_color": "#C9CDCD",
            "sky_blue_color": "#4072F1",
            "grey_blue_color": "#9FBBD2"
        }

        self.create_widgets()

    def create_widgets(self):
        # Add big Label with bold font
        title_label = tk.CTkLabel(master=self.master, text="Settings", font=("Noto Sans", 46, "bold"),
                                  text_color="black")
        title_label.place(relx=0.5, rely=0.05, anchor=tk_standard.N)
        title_label.pack(pady=10, padx=10)

        # Example of setting toggle button
        dark_mode_label = tk.CTkLabel(master=self.master, text="Dark Mode", font=("Noto Sans", 22, "bold"),
                                      text_color="black")
        dark_mode_label.pack(pady=(20, 10), padx=10)

        # add radio buttons

        radio_var = tk.StringVar(value="Off")
        dark_mode_toggle = tk.CTkRadioButton(master=self.master, text="On", font=("Noto Sans", 18),
                                             text_color="black",
                                             fg_color=self.my_colors["dark_grey_color"],
                                             variable=radio_var, value="On")
        dark_mode_toggle.pack(pady=5, padx=10)

        dark_mode_toggle = tk.CTkRadioButton(master=self.master, text="Off", font=("Noto Sans", 18),
                                             text_color="black",
                                             fg_color=self.my_colors["dark_grey_color"],
                                             variable=radio_var, value="Off")
        dark_mode_toggle.pack(pady=5, padx=10)

        variables = {
            'USD': 4.0124,
            'EUR': 4.3242,
            'GBP': 5.0152,
            'JPY': 0.02625,
            'CNY': 0.5446,
            'RUB': 0.04330,
        }

        list_of_currencies = list(variables.keys())
        # Add entry widget
        main_currency_label = tk.CTkLabel(master=self.master, text="Choose your main currency", font=("Noto Sans", 22, "bold"),
                                          text_color="black")
        main_currency_label.pack(pady=(45, 10), padx=10)
        main_currency_option_menu = tk.CTkOptionMenu(master=self.master, values=list_of_currencies, font=("Noto Sans", 20),
                                                        fg_color=self.my_colors["sky_blue_color"], bg_color=self.my_colors["light_grey_color"])
        main_currency_option_menu.pack(pady=2, padx=10)
        main_currency_info_label = tk.CTkLabel(master=self.master, text="This currency will be displayed on the home screen",
                                               font=("Noto Sans", 16), text_color="black")
        main_currency_info_label.pack(pady=2, padx=10)

        # Example of setting button
        save_button = tk.CTkButton(master=self.master, text="Save", font=("Noto Sans", 22, "bold"),
                                   fg_color=self.my_colors["dark_grey_color"],
                                   width=180, height=40)
        save_button.pack(pady=(5, 40), padx=10, side=tk_standard.BOTTOM)

        # SET CURSOR ON BUTTONS
        save_button.configure(cursor="hand2")

        # BINDING EVENTS
        # Zdefiniuj funkcję, która zostanie wywołana po naciśnięciu przycisku "Save"
        save_button.bind("<Button-1>", lambda event:
                         self.save_settings(main_currency_option_menu.get()))

    def save_settings(self, new_main_currency):

        # set light mode
        # tk.set_appearance_mode("light")

        self.user_info["main_currency"] = new_main_currency

        print("Settings saved!")
