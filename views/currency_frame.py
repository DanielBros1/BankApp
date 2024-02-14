import customtkinter as tk
from PIL import Image
import tkinter as tk_standard


class CurrencyFrame:
    def __init__(self, master):
        self.master = master
        self.my_colors = {
            # DARK MODE
            "dark_grey_color": "#2B2B2B",
            "very_dark_grey_color": "#1E1E1E",
            "some_dark_grey_color": "#4A4A4A",
            # LIGHT MODE
            "light_grey_color": "#C9CDCD",
            "sky_blue_color": "#4072F1",
            "grey_blue_color": "#9FBBD2"
        }
        self.currencies = [
            {
                "logo": self.load_image("cur_dolar"),
                "value": "4.0124 PLN"
            },
            {
                "logo": self.load_image("cur_euro"),
                "value": "4.3242 PLN"
            },
            {
                "logo": self.load_image("cur_pound"),
                "value": "5.0152 PLN"
            },
            {
                "logo": self.load_image("cur_yen"),
                "value": "0.02625 PLN"
            },
            {
                "logo": self.load_image("cur_yuan"),
                "value": "0.5446 PLN"
            },
            {
                "logo": self.load_image("cur_ruble"),
                "value": "0.04330 PLN"
            }
        ]
        self.create_widgets()

    def load_image(self, image_name):
        white_image = Image.open(f"images/{image_name}_black.png")
        #    white_image = white_image.resize((200, 200))  # Resize the image
        #    black_image = Image.open(f"images/{image_name}_white.png")
        return tk.CTkImage(light_image=white_image, dark_image=white_image, size=(150, 134))

    # def create_widgets(self):
    #
    #     # Add big Label with bold font
    #     title_label = tk.CTkLabel(master=self.master, text="Currency Exchange", font=("Noto Sans", 46, "bold"),
    #                               text_color="black")
    #     title_label.place(relx=0.5, rely=0.05, anchor=tk_standard.N)
    #     title_label.pack(pady=10, padx=10)
    #
    #     # Create scrollable frame
    #     self.currency_scrollable_frame = tk.CTkScrollableFrame(master=self.master)
    #     self.currency_scrollable_frame.place(relwidth=1, relheight=0.85, relx=0, rely=0.15)
    #
    #
    #     for i, currency_data in enumerate(self.currencies):
    #         # Create widget for each currency
    #         currency_frame = tk.CTkFrame(master=self.currency_scrollable_frame)
    #         rel_x = 0.12 + i % 2 * 0.55  # Dynamic placement based on index
    #         rel_y = 0.15 + i // 2 * 0.28  # Dynamic placement based on index
    #         currency_frame.place(relwidth=0.2, relheight=0.22, relx=rel_x, rely=rel_y)
    #
    #         currency_logo_imag = currency_data['logo']
    #         currency_value = currency_data['value']
    #
    #         currency_logo_label = tk.CTkLabel(master=self.currency_scrollable_frame, image=currency_logo_imag, compound=tk.TOP,
    #                                           text=currency_value,
    #                                           text_color='white', font=('Noto Sans', 26))
    #         currency_logo_label.pack(pady=3, padx=3, side=tk.BOTTOM)

    def create_widgets(self):
        # Add big Label with bold font
        title_label = tk.CTkLabel(master=self.master, text="Currency Exchange", font=("Noto Sans", 46, "bold"),
                                  text_color="black")
        title_label.place(relx=0.5, rely=0.05, anchor=tk_standard.N)
        title_label.pack(pady=10, padx=10)

        # TOP FRAME - LABELS
        top_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["sky_blue_color"])
        top_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.15)

        amount_label = tk.CTkLabel(master=top_frame, text="AMOUNT", font=("Noto Sans", 22, "bold"), text_color="black")
        amount_label.pack(padx=10, pady=2, side=tk_standard.LEFT)
        to_label = tk.CTkLabel(master=top_frame, text="TO", font=("Noto Sans", 22, "bold"), text_color="black")
        to_label.pack(padx=10, pady=2, side=tk_standard.RIGHT)
        from_label = tk.CTkLabel(master=top_frame, text="FROM", font=("Noto Sans", 22, "bold"), text_color="black")
        from_label.pack(padx=10, pady=2, side=tk_standard.TOP)

        # MIDDLE FRAME - ENTRY and OPTION MENU
        middle_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["sky_blue_color"])
        middle_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.22)
        #  variables = ["USD", "EUR", "GBP", "JPY", "CNY", "RUB"]

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
        amount_entry = tk.CTkEntry(master=middle_frame, font=("Noto Sans", 18))
        amount_entry.pack(pady=2, padx=10, side=tk_standard.LEFT)
        option_menu_to = tk.CTkOptionMenu(master=middle_frame, values=list_of_currencies, font=("Noto Sans", 20))
        option_menu_to.pack(pady=2, padx=10, side=tk_standard.RIGHT)
        option_menu_from = tk.CTkOptionMenu(master=middle_frame, values=list_of_currencies, font=("Noto Sans", 20))
        option_menu_from.pack(pady=2, padx=10, side=tk_standard.TOP)

        # BOTTOM FRAME - CALCULATE BUTTON
        bottom_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["sky_blue_color"])
        bottom_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.30)

        result_label = tk.CTkLabel(master=bottom_frame, text="0", font=("Noto Sans", 22, "bold"), text_color="black")
        result_label.pack(pady=2, padx=10, side=tk_standard.LEFT)

        # Add onclick event to calculate button
        calculate_button = tk.CTkButton(master=bottom_frame, text="Calculate", font=("Noto Sans", 22, "bold"),
                                        fg_color=self.my_colors["dark_grey_color"])
        calculate_button.pack(pady=2, padx=10, side=tk_standard.RIGHT)

        # ONCLICK EVENT
        # Pobierz wartosc

        # Sprawdz czy wartosc z option_menu_to jest w slowniku
        # Jesli tak to oblicz wartosc

        self.exchange_rate = variables.get(option_menu_to.get())

        # SET CURSOR ON CALCULATE BUTTON
        calculate_button.configure(cursor="hand2")

        calculate_button.bind("<Button-1>",
                              lambda event: self.calculate_result(event, variables, amount_entry, option_menu_to,
                                                                  option_menu_from, result_label))

        # First currency
        currency_frame1 = tk.CTkFrame(master=self.master)
        currency_frame1.place(relwidth=0.2, relheight=0.22, relx=0.4, rely=0.43)

        currency_logo_imag1 = self.currencies[0]['logo']
        currency_value1 = self.currencies[0]['value']

        currency_logo_label1 = tk.CTkLabel(master=currency_frame1, image=currency_logo_imag1, compound=tk.TOP,
                                           text=currency_value1,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label1.pack(pady=3, padx=3, side=tk.BOTTOM)

        # Second currency
        currency_frame2 = tk.CTkFrame(master=self.master)
        currency_frame2.place(relwidth=0.2, relheight=0.22, relx=0.4, rely=0.71)

        currency_logo_imag2 = self.currencies[1]['logo']
        currency_value2 = self.currencies[1]['value']

        currency_logo_label2 = tk.CTkLabel(master=currency_frame2, image=currency_logo_imag2, compound=tk.TOP,
                                           text=currency_value2,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label2.pack(pady=3, padx=3, side=tk.BOTTOM)

        # Third currency
        currency_frame3 = tk.CTkFrame(master=self.master)
        currency_frame3.place(relwidth=0.2, relheight=0.22, relx=0.12, rely=0.43)

        currency_logo_imag3 = self.currencies[2]['logo']
        currency_value3 = self.currencies[2]['value']

        currency_logo_label3 = tk.CTkLabel(master=currency_frame3, image=currency_logo_imag3, compound=tk.TOP,
                                           text=currency_value3,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label3.pack(pady=3, padx=3, side=tk.BOTTOM)

        # Fourth currency
        currency_frame4 = tk.CTkFrame(master=self.master)
        currency_frame4.place(relwidth=0.2, relheight=0.22, relx=0.67, rely=0.43)

        currency_logo_imag4 = self.currencies[3]['logo']
        currency_value4 = self.currencies[3]['value']

        currency_logo_label4 = tk.CTkLabel(master=currency_frame4, image=currency_logo_imag4, compound=tk.TOP,
                                           text=currency_value4,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label4.pack(pady=3, padx=3, side=tk.BOTTOM)

        # Fifth currency
        currency_frame5 = tk.CTkFrame(master=self.master)
        currency_frame5.place(relwidth=0.2, relheight=0.22, relx=0.12, rely=0.71)

        currency_logo_imag5 = self.currencies[4]['logo']
        currency_value5 = self.currencies[4]['value']

        currency_logo_label5 = tk.CTkLabel(master=currency_frame5, image=currency_logo_imag5, compound=tk.TOP,
                                           text=currency_value5,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label5.pack(pady=3, padx=3, side=tk.BOTTOM)

        # Sixth currency
        currency_frame6 = tk.CTkFrame(master=self.master)
        currency_frame6.place(relwidth=0.2, relheight=0.22, relx=0.67, rely=0.71)

        currency_logo_imag6 = self.currencies[5]['logo']
        currency_value6 = self.currencies[5]['value']

        currency_logo_label6 = tk.CTkLabel(master=currency_frame6, image=currency_logo_imag6, compound=tk.TOP,
                                           text=currency_value6,
                                           text_color='white', font=('Noto Sans', 26))
        currency_logo_label6.pack(pady=3, padx=3, side=tk.BOTTOM)


        # SET CURSOR ON CURRNECY FRAMES
        currency_frame1.configure(cursor="hand2")
        currency_frame2.configure(cursor="hand2")
        currency_frame3.configure(cursor="hand2")
        currency_frame4.configure(cursor="hand2")
        currency_frame5.configure(cursor="hand2")
        currency_frame6.configure(cursor="hand2")

        # HOVER EFFECTS
        currency_frame1.bind("<Enter>",
                             lambda event: currency_frame1.configure(fg_color=self.my_colors["sky_blue_color"]))
        currency_logo_label1.bind("<Enter>",
                                  lambda event: currency_frame1.configure(fg_color=self.my_colors["sky_blue_color"]))
        currency_frame1.bind("<Leave>",
                             lambda event: currency_frame1.configure(fg_color=self.my_colors["dark_grey_color"]))
        currency_logo_label1.bind("<Leave>",
                                  lambda event: currency_frame1.configure(fg_color=self.my_colors["dark_grey_color"]))

        currency_frame2.bind("<Enter>",
                             lambda event: currency_frame2.configure(fg_color=self.my_colors["sky_blue_color"]))
        currency_logo_label2.bind("<Enter>",
                                  lambda event: currency_frame2.configure(fg_color=self.my_colors["sky_blue_color"]))
        currency_frame2.bind("<Leave>",
                             lambda event: currency_frame2.configure(fg_color=self.my_colors["dark_grey_color"]))
        currency_logo_label2.bind("<Leave>",
                                  lambda event: currency_frame2.configure(fg_color=self.my_colors["dark_grey_color"]))

        # BINDING EVENTS
        # Stwórz nowe okno z wykresem
        currency_logo_label1.bind("<Button-1>", lambda event: self.call_currency_exchange_window(currency_value1))

    def calculate_result(self, event, variables, amount_entry, option_menu_to, option_menu_from, result_label):
        self.exchange_rate = variables.get(option_menu_from.get()) / variables.get(option_menu_to.get())
        print(self.exchange_rate)

        try:
            entry_value = round(float(amount_entry.get()), 4)
            result_value = round(float(amount_entry.get()) * self.exchange_rate, 4)
            result_label.configure(
                text=f"{entry_value} {option_menu_from.get()} = {result_value} {option_menu_to.get()}")
        except ValueError:
            entry_value = "Niepoprawna wartość!"
            result_value = ""
            result_label.configure(
                text=f"{entry_value}")




    def call_currency_exchange_window(self, currency_value):
        currency_value_sell = currency_value.split(" ")[0]
        # Zaokraglij do 4 miejsc po przecinku
        currency_value_sell = round(float(currency_value_sell) - (float(currency_value_sell) * 0.01), 4)
        currency_value_buy = currency_value.split(" ")[0]
        currency_value_buy = round(float(currency_value_buy) + (float(currency_value_buy) * 0.01), 4)

        # Create new window
        currency_exchange_window = tk.CTk()
        currency_exchange_window.geometry("450x320")

        left_frame = tk.CTkFrame(master=currency_exchange_window)
        left_frame.pack(pady=5, side=tk_standard.LEFT, fill=tk_standard.BOTH, expand=True)

        right_frame = tk.CTkFrame(master=currency_exchange_window)
        right_frame.pack(pady=5, side=tk_standard.RIGHT, fill=tk_standard.BOTH, expand=True)

        sell_info_label = tk.CTkLabel(left_frame, text="Sell", font=("Noto Sans", 26, "bold"))
        sell_info_label.pack(pady=10, padx=10)

        sell_value_label = tk.CTkLabel(left_frame, text=f'Rate: {currency_value_sell}', font=("Noto Sans", 20))
        sell_value_label.pack(padx=10)

        buy_info_label = tk.CTkLabel(right_frame, text="Buy", font=("Noto Sans", 26, "bold"))
        buy_info_label.pack(pady=10, padx=10)

        buy_value_label = tk.CTkLabel(right_frame, text=f'Rate: {currency_value_buy}', font=("Noto Sans", 20))
        buy_value_label.pack(padx=10)

        # # Create an entry widget
        # currency_entry = tk.CTkEntry(currency_exchange_frame)
        # currency_entry.pack(pady=10, padx=10)
        #
        # value_of_currency = currency_value.split(" ")[0]
        # print(value_of_currency)
        #
        # # accept button widget
        # accept_button = tk.CTkButton(currency_exchange_frame, text="Calculate", command=lambda: print(currency_entry.get()))
        # accept_button.pack(padx=10, pady=10)
        #
        # # deny button widget
        # deny_button = tk.CTkButton(currency_exchange_frame, text="Deny", command=currency_exchange_window.destroy)
        # deny_button.pack(padx=10, pady=10)

        # display the frame
        currency_exchange_window.mainloop()

        print(currency_value)
