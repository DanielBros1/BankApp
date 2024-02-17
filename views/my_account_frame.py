import sqlite3

import customtkinter as tk
from PIL import Image, ImageTk

MAIN_FONT = "Noto Sans"


class MyAccountFrame():
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
        self.currencies = ["USD", "EUR", "GBP", "JPY", "CNY", "RUB"]
        self.create_widgets()

    def load_image(image_name):
        white_image = Image.open(f"images/{image_name}_black.png")
        return tk.CTkImage(light_image=white_image, dark_image=white_image, size=(150, 134))

    def create_widgets(self):
        # First area: 'Your account'
        account_title_frame = tk.CTkFrame(master=self.master)
        account_title_frame.place(relwidth=1.0, relheight=0.15, relx=0, rely=0)
        account_title_frame.configure(fg_color=self.my_colors['light_grey_color'])
        account_title_label = tk.CTkLabel(master=account_title_frame, text="Your Account", font=(MAIN_FONT, 36, "bold"),
                                          text_color='black')
        account_title_label.pack(pady=20)

        # Second area: Image with credit card

        credit_card_frame = tk.CTkFrame(master=self.master)
        credit_card_frame.place(relwidth=1.0, relheight=0.35, relx=0, rely=0.15)
        credit_card_frame.configure(fg_color=self.my_colors['light_grey_color'])
        credit_card_image = Image.open("credit_card.jpg")
        credit_card_photo = tk.CTkImage(light_image=credit_card_image, dark_image=credit_card_image, size=(340, 220))
        credit_card_label = tk.CTkLabel(master=credit_card_frame, image=credit_card_photo, text="")
        credit_card_label.image = credit_card_photo
        credit_card_label.pack()


        # Third area: Information about all currencies
        label_currency_info_frame = tk.CTkFrame(master=self.master)
        label_currency_info_frame.place(relwidth=1.0, relheight=0.05, relx=0, rely=0.50)
        label_currency_info_frame.configure(fg_color=self.my_colors['light_grey_color'])
        currency_info_label = tk.CTkLabel(master=label_currency_info_frame, text="ACCOUNT BALANCE - CURRENCIES",
                                          font=(MAIN_FONT, 26, "bold"), text_color='black')
        currency_info_label.pack(pady=5)

        # Fourth area: currency information
        currency_info_frame = tk.CTkFrame(master=self.master)
        currency_info_frame.place(relwidth=1.0, relheight=0.35, relx=0, rely=0.55)
        currency_info_frame.configure(fg_color=self.my_colors['light_grey_color'])

        self.fetch_and_draw_currency_info(currency_info_frame)

        # Add button showing all new frame with all transactions
        transactions_button = tk.CTkButton(master=self.master, text="Show all transactions", font=(MAIN_FONT, 20, "bold"),
                                           command=self.show_transactions)
        transactions_button.place(relwidth=0.8, relheight=0.08, relx=0.10, rely=0.90)
        transactions_button.configure(fg_color=self.my_colors['dark_grey_color'],
                                      bg_color=self.my_colors['sky_blue_color'])

    def show_transactions(self):
        print("Showing all transactions")
        conn = sqlite3.connect('currency_exchange.db')
        cursor = conn.cursor()

        # Get username from user_info
        username = self.user_info['username']

        # Get user id from database
        cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
        user_id = cursor.fetchone()[0]

        # Get user account by user id
        cursor.execute(f"SELECT id FROM accounts WHERE user_id = {user_id}")
        account_id = cursor.fetchone()[0]

        # Get all transactions by user_account_id
        cursor.execute(f"SELECT * FROM transactions WHERE id_account = {account_id}")
        transactions = cursor.fetchall()

        # Columns in transactions: id, id_account, date, amount, currency (1, 2, 3, 4, 5, 6)
        transactions = [list(transaction) for transaction in transactions]
        for transaction in transactions:
            transaction[2] = transaction[2].split(" ")[0]

        # Create new window with all transactions

        # Create new window

        transactions_window = tk.CTk()
        transactions_window.geometry("800x600")
        transactions_window.configure(fg_color=self.my_colors['dark_grey_color'])
        transactions_frame = tk.CTkScrollableFrame(master=transactions_window)
        transactions_frame.place(relwidth=1.0, relheight=1.0, relx=0, rely=0)
        transactions_frame.configure(fg_color=self.my_colors['light_grey_color'])

        i = 1  # Liczba porzadkowa transakcji
        # Create labels with all transactions - liczba porzadkowa, data, kwota, waluta
        for transaction in transactions:
            # Determine text color based on transaction type
            text_color = "green" if transaction[3] > 0 else "red"

            transaction_label = tk.CTkLabel(master=transactions_frame,
                                            text=f"{i}. {transaction[2]}:  "
                                                 f"{transaction[3]} {self.currencies[transaction[4] - 1]}",
                                            font=(MAIN_FONT, 24, "bold"),  # Increase font size
                                            text_color=text_color,  # Set text color based on transaction type
                                            # bg_color=self.my_colors['sky_blue_color'],  # Set background color
                                            padx=10,  # Add horizontal padding
                                            pady=10)  # Add vertical padding
            transaction_label.pack(pady=10, padx=30)  # Increase padding around the label
            i += 1
        transactions_window.mainloop()

    def fetch_and_draw_currency_info(self, currency_info_frame):
        conn = sqlite3.connect('currency_exchange.db')
        cursor = conn.cursor()

        # Get username from user_info
        username = self.user_info['username']

        # Get user id from database
        cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
        user_id = cursor.fetchone()[0]

        # Get user account by user id
        cursor.execute(f"SELECT * FROM accounts WHERE user_id = {user_id}")
        account = cursor.fetchone()

        # Columns in account: id, user_id, balance_usd, balance_eur, balance_gbp, balance_jpy, balance_cny, balance_rub
        account = account[2:]  # Delete two first columns (id, user_id)

        for currency in self.currencies:
            currency_index = self.currencies.index(currency)
            currency_info_label = tk.CTkLabel(master=currency_info_frame,
                                              text=f"{currency}: {account[currency_index]}",
                                              font=(MAIN_FONT, 20, "bold"),
                                              text_color=self.my_colors['dark_grey_color'])
            currency_info_label.pack(pady=5, padx=30)

        cursor.close()
        conn.close()
