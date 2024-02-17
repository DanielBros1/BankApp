import sqlite3
from datetime import datetime

import customtkinter as tk
import pandas as pd
from PIL import Image
import tkinter as tk_standard
import requests

from CTkMessagebox import CTkMessagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

MAIN_FONT = "Noto Sans"
CLICK = "<Button-1>"
HOVER = "<Enter>"
LEAVE = "<Leave>"


class CurrencyFrame:
    def __init__(self, master, user_info):
        self.master = master
        self.user_info = user_info
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
                "name": "USD",
                "logo": self.load_image("cur_dolar"),
                "index": 1
            },
            {
                "name": "EUR",
                "logo": self.load_image("cur_euro"),
                "index": 2
            },
            {
                "name": "GBP",
                "logo": self.load_image("cur_pound"),
                "index": 3
            },
            {
                "name": "JPY",
                "logo": self.load_image("cur_yen"),
                "index": 4
            },
            {
                "name": "CNY",
                "logo": self.load_image("cur_yuan"),
                "index": 5
            },
            {
                "name": "RUB",
                "logo": self.load_image("cur_ruble"),
                "index": 6
            }
        ]
        self.fetch_exchange_rates()
        self.create_widgets()

    def fetch_exchange_rates(self):

        def fetch_single_rate(base_currency, target_currency="PLN"):
            amount = 1
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"
            response = requests.get(url)
            data = response.json()
            return data['rates'][target_currency]

        self.exchange_rates = {
            "USD": fetch_single_rate("USD"),
            "EUR": fetch_single_rate("EUR"),
            "GBP": fetch_single_rate("GBP"),
            "JPY": fetch_single_rate("JPY"),
            "CNY": fetch_single_rate("CNY"),
            "RUB": 0.04330  # RUB is not supported by the API
        }
        print(self.exchange_rates)

        # Dodaj do currencies
        for currency in self.currencies:
            currency["value"] = f"{self.exchange_rates[currency['name']]} PLN"

        print(self.currencies)

    @staticmethod
    def create_historical_data(base_currency, target_currency="PLN"):
        # Fetch historical data from API
        url = f"https://api.frankfurter.app/2020-01-01..?from={base_currency}&to={target_currency}"

        response = requests.get(url)
        data = response.json()

        # Convert data to pandas DataFrame
        df = pd.DataFrame(data["rates"].items(), columns=["Date", "Rate"])
        df["Date"] = pd.to_datetime(df["Date"])
        df["Rate"] = df["Rate"].apply(lambda x: x[target_currency])

        # Create figure
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        ax.plot(df["Date"], df["Rate"])
        ax.set_xlabel("Date", fontsize=20, fontweight='bold', color='black')
        ax.set_ylabel(f"Exchange Rate ({base_currency}/{target_currency})", fontsize=20,
                      fontweight='bold', color='black')
        ax.set_title(f"Historical Exchange Rate of {base_currency} to {target_currency}", fontsize=22,
                     fontweight='bold', color='black')
        ax.grid(True)
        # Set font size for x-axis and y-axis labels
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=22)
        return fig

    @staticmethod
    def load_image(image_name):
        white_image = Image.open(f"images/{image_name}_black.png")
        return tk.CTkImage(light_image=white_image, dark_image=white_image, size=(150, 134))

    def create_widgets(self):
        # Add big Label with bold font
        title_label = tk.CTkLabel(master=self.master, text="Currency Exchange", font=(MAIN_FONT, 46, "bold"),
                                  text_color="black")
        title_label.place(relx=0.5, rely=0.05, anchor=tk_standard.N)
        title_label.pack(pady=10, padx=10)

        # TOP FRAME - LABELS
        top_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["sky_blue_color"])
        top_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.14)

        amount_label = tk.CTkLabel(master=top_frame, text="AMOUNT", font=(MAIN_FONT, 22, "bold"), text_color="black")
        amount_label.pack(padx=10, pady=2, side=tk_standard.LEFT)
        to_label = tk.CTkLabel(master=top_frame, text="TO", font=(MAIN_FONT, 22, "bold"), text_color="black")
        to_label.pack(padx=10, pady=2, side=tk_standard.RIGHT)
        from_label = tk.CTkLabel(master=top_frame, text="FROM", font=(MAIN_FONT, 22, "bold"), text_color="black")
        from_label.pack(padx=10, pady=2, side=tk_standard.TOP)

        # MIDDLE FRAME - ENTRY and OPTION MENU
        middle_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["grey_blue_color"])
        middle_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.20)

        list_of_currencies = []

        for currency in self.currencies:
            list_of_currencies.append(currency['name'])

        # Add entry widget
        amount_entry = tk.CTkEntry(master=middle_frame, font=(MAIN_FONT, 18))
        amount_entry.pack(pady=2, padx=10, side=tk_standard.LEFT)
        option_menu_to = tk.CTkOptionMenu(master=middle_frame, values=list_of_currencies, font=(MAIN_FONT, 20))
        option_menu_to.pack(pady=2, padx=10, side=tk_standard.RIGHT)
        option_menu_from = tk.CTkOptionMenu(master=middle_frame, values=list_of_currencies, font=(MAIN_FONT, 20))
        option_menu_from.pack(pady=2, padx=10, side=tk_standard.TOP)

        # BOTTOM FRAME - CALCULATE BUTTON
        bottom_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["grey_blue_color"])
        bottom_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.26)

        result_label = tk.CTkLabel(master=bottom_frame, text="0", font=(MAIN_FONT, 22, "bold"), text_color="black")
        result_label.pack(pady=2, padx=10, side=tk_standard.LEFT)

        # Add onclick event to calculate button
        calculate_button = tk.CTkButton(master=bottom_frame, text="Calculate", font=(MAIN_FONT, 22, "bold"),
                                        fg_color=self.my_colors["dark_grey_color"])
        calculate_button.pack(pady=2, padx=10, side=tk_standard.RIGHT)

        # MOST BOTTOM FRAME - EXCHANGE BUTTON
        exchange_frame = tk.CTkFrame(master=self.master, fg_color=self.my_colors["light_grey_color"])
        exchange_frame.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.32)

        exchange_button = tk.CTkButton(master=exchange_frame, text="Exchange", font=(MAIN_FONT, 22, "bold"),
                                       fg_color=self.my_colors["dark_grey_color"])
        exchange_button.pack(pady=2, padx=10, side=tk_standard.TOP)

        # SET CURSOR ON BUTTONS
        calculate_button.configure(cursor="hand2")
        exchange_button.configure(cursor="hand2")

        calculate_button.bind(CLICK,
                              lambda event: self.calculate_result(event, amount_entry, option_menu_to,
                                                                  option_menu_from, result_label))
        # Do funkcji przekazujemy wartosc wymiany i dwie waluty
        exchange_button.bind(CLICK, lambda event: self.exchange_function(
            amount_entry.get(), option_menu_to.get(), option_menu_from.get()))

        relx_positions = [0.4, 0.4, 0.12, 0.67, 0.12, 0.67]
        rely_positions = [0.43, 0.71, 0.43, 0.43, 0.71, 0.71]

        for i, currency_data in enumerate(self.currencies):
            currency_frame = tk.CTkFrame(master=self.master)
            currency_frame.place(relwidth=0.2, relheight=0.22, relx=relx_positions[i], rely=rely_positions[i])

            # Extract data for the currency
            currency_logo_img = currency_data['logo']
            currency_value = currency_data['value']
            currency_name = currency_data['name']

            currency_logo_label = tk.CTkLabel(master=currency_frame, image=currency_logo_img, compound=tk.TOP,
                                              text=currency_value, text_color='white', font=(MAIN_FONT, 26))
            currency_logo_label.pack(pady=3, padx=3, side=tk.BOTTOM)

            # BIND EVENTS to open currency exchange window
            currency_logo_label.bind(CLICK, lambda event, value=currency_value,
                                                   name=currency_name: self.call_currency_exchange_window(value, name))

            currency_frame.configure(cursor="hand2")

            # HOVER EFFECTS to change frame color
            currency_frame.bind(HOVER,
                                lambda event, frame=currency_frame:
                                frame.configure(fg_color=self.my_colors["sky_blue_color"]))
            currency_logo_label.bind(HOVER,
                                     lambda event, frame=currency_frame:
                                     frame.configure(fg_color=self.my_colors["sky_blue_color"]))
            currency_frame.bind(LEAVE,
                                lambda event, frame=currency_frame:
                                frame.configure(fg_color=self.my_colors["dark_grey_color"]))
            currency_logo_label.bind(LEAVE,
                                     lambda event, frame=currency_frame:
                                     frame.configure(fg_color=self.my_colors["dark_grey_color"]))

    def exchange_function(self, amount, currency_to, currency_from):
        conn = sqlite3.connect('currency_exchange.db')
        c = conn.cursor()

        # Check if user has enough money
        c.execute("SELECT id FROM users WHERE username = ?", (self.user_info["username"],))
        user = c.fetchone()

        print(user)

        # find user account using user id
        c.execute("SELECT * FROM accounts WHERE user_id = ?", (user[0],))
        account = c.fetchone()  # Konto bankowe uzytkownika

        print(account)

        currency_out_column = f"balance_{currency_from}"
        currency_in_column = f"balance_{currency_to}"

        # Check if user has enough money
        # Fetch user currency_from balance
        c.execute(f"SELECT {currency_out_column} FROM accounts WHERE user_id = ?", (user[0],))
        currency_out_balance = c.fetchone()

        if currency_out_balance[0] < float(amount):
            message_box = CTkMessagebox(title="Error", message="You don't have enough money to exchange!",
                                        icon="cancel")

            # Wait for user interaction and then 'return'
            self.master.wait_window(message_box)
            return

        amount_after_exchange = round(
            float(amount) * self.exchange_rates[currency_from] / self.exchange_rates[currency_to], 4)
        print(amount_after_exchange)

        # WITHDRAW MONEY FROM CURRENCY_FROM IN ACCOUNTS TABLE
        c.execute(f"UPDATE accounts SET {currency_out_column} = "
                  f"{currency_out_column} - ? WHERE user_id = ?", (amount, user[0]))
        # DEPOSIT MONEY TO CURRENCY_TO IN ACCOUNTS TABLE
        c.execute(f"UPDATE accounts SET {currency_in_column} = "
                  f"{currency_in_column} + ? WHERE user_id = ?", (amount_after_exchange, user[0]))

        currency_from_index = self.get_currency_index(currency_from)
        currency_to_index = self.get_currency_index(currency_to)


        print(
            f"Data added to transactions table - {account[0]}, {datetime.now().strftime('%Y-%m-%d')}, "
            f"{amount}, {currency_from_index}")

        # ADD TO TRANSACTIONS TABLE
        c.execute("INSERT INTO transactions (id_account, date, amount, currency) VALUES (?, ?, ?, ?)",
                  (account[0], datetime.now().strftime("%Y-%m-%d"), -float(amount), currency_from_index))

        c.execute("INSERT INTO transactions (id_account, date, amount, currency) VALUES (?, ?, ?, ?)",
                  (account[0], datetime.now().strftime("%Y-%m-%d"), amount_after_exchange, currency_to_index))
        conn.commit()

        c.close()
        conn.close()

        CTkMessagebox(title="Success", message="Exchange completed successfully!",
                      icon="check")

    def calculate_result(self, event, amount_entry, option_menu_to, option_menu_from, result_label):

        exchange_rate = self.exchange_rates[option_menu_from.get()] / self.exchange_rates[option_menu_to.get()]

        try:
            entry_value = round(float(amount_entry.get()), 2)
            result_value = round(float(amount_entry.get()) * exchange_rate, 2)
            result_label.configure(
                text=f"{entry_value} {option_menu_from.get()} = {result_value} {option_menu_to.get()}")
        except ValueError:
            entry_value = "Niepoprawna wartość!"
            result_label.configure(
                text=f"{entry_value}")

    def call_currency_exchange_window(self, currency_value, currency_name):
        currency_value_sell = currency_value.split(" ")[0]
        # Zaokraglij do 2 miejsc po przecinku
        currency_value_sell = round(float(currency_value_sell) - (float(currency_value_sell) * 0.01), 4)
        currency_value_buy = currency_value.split(" ")[0]
        currency_value_buy = round(float(currency_value_buy) + (float(currency_value_buy) * 0.01), 4)

        # Create new window
        currency_exchange_window = tk.CTk()
        currency_exchange_window.geometry("500x450")

        buy_frame = tk.CTkFrame(master=currency_exchange_window)
        buy_frame.pack(pady=5, side=tk_standard.BOTTOM, fill=tk_standard.BOTH)

        sell_frame = tk.CTkFrame(master=currency_exchange_window)
        sell_frame.pack(pady=5, side=tk_standard.TOP, fill=tk_standard.BOTH)

        sell_info_label = tk.CTkLabel(buy_frame, text="Sell", font=(MAIN_FONT, 22, "bold"))
        sell_info_label.pack(pady=4, padx=10)

        buy_info_label = tk.CTkLabel(sell_frame, text="Buy", font=(MAIN_FONT, 22, "bold"))
        buy_info_label.pack(pady=4, padx=10)

        fig = self.create_historical_data(currency_name)
        canvas = FigureCanvasTkAgg(fig, master=currency_exchange_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk_standard.BOTTOM, fill=tk_standard.BOTH, expand=1)

        # display the frame
        currency_exchange_window.mainloop()

        print(currency_value)

    def get_currency_index(self, currency_name):
        for currency in self.currencies:
            if currency['name'] == currency_name:
                return currency['index']
        return None
