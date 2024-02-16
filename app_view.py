import sqlite3
from datetime import datetime

import customtkinter as tk
from PIL import ImageTk, Image
from CTkTable import *
import requests
from CTkMessagebox import CTkMessagebox

from views.currency_frame import CurrencyFrame
from views.settings_frame import SettingsFrame


class AppView:
    def __init__(self, frame, username):
        self.frame = frame
        self.username = username
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
        print(self.my_colors.get("dark_grey_color"))
        self.user_info = {
            "username": self.username,
            "balance": self.fetch_user_balance(self.username),
            "transactions": self.fetch_user_transactions(self.username),
            "main_currency": "EUR"
        }

        self.setup_applications_widgets()

    def fetch_user_balance(self, username):
        # Connect to database and fetch user balance
        conn = sqlite3.connect('currency_exchange.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM accounts "
                       f"WHERE user_id = (SELECT id FROM users WHERE username = '{username}')")

        user_result = cursor.fetchone()

        # Fetch all currencies
        cursor.execute(f"SELECT id, code FROM currencies")
        currencies = cursor.fetchall()

        cursor.close()
        conn.close()

        # Stworzenie slownika wartosciami posiadania walut przez uzytkownika
        # example result: {'USD': 100, 'EUR': 200, 'GBP': 300, 'JPY': 400, 'CNY': 500, 'RUB': 600}
        currencies_dict = {}
        for i in range(6):
            currencies_dict.update(
                {currencies[i][1]: user_result[i+2]}
            )

        return currencies_dict


    def test_widget(self, base_currency, target_currency, amount):
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"
        response = requests.get(url)
        data = response.json()
        print(response.status_code)
        print(f"amout: {amount} {base_currency} is {response.json()['rates'][target_currency]} {target_currency}")
        return data['rates'][target_currency]

    def destroy_widgets(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def setup_applications_widgets(self):
        # # DARK MODE
        # dark_grey_color = "#2B2B2B"
        # very_dark_grey_color = "#1E1E1E"
        # some_dark_grey_color = "#4A4A4A"
        # # LIGHT MODE
        # light_grey_color = "#C9CDCD"
        # sky_blue_color = "#4072F1"
        # grey_blue_color = "#9FBBD2"

        app_window = self.frame.master
        app_window.geometry("1280x720")
        app_window.title("Banking App")

        # Utworzenie trzech obszarów z odpowiednimi szerokościami
        self.left_frame = tk.CTkFrame(master=app_window)
        self.left_frame.place(relwidth=0.15, relheight=1.0, relx=0, rely=0)
        #  left_frame.configure(fg_color=dark_grey_color)
        self.left_frame.configure(fg_color=self.my_colors.get("sky_blue_color"))
        self.left_frame.configure(cursor="mouse")

        self.center_frame = tk.CTkFrame(master=app_window)
        self.center_frame.place(relwidth=0.60, relheight=1.0, relx=0.15, rely=0)
        # center_frame.configure(fg_color=some_dark_grey_color)
        self.center_frame.configure(fg_color=self.my_colors.get("light_grey_color"))

        right_frame = tk.CTkFrame(master=app_window)
        right_frame.place(relwidth=0.25, relheight=1.0, relx=0.75, rely=0)
        # right_frame.configure(fg_color=very_dark_grey_color)
        right_frame.configure(fg_color=self.my_colors.get("grey_blue_color"))

        account_imag, add_money_imag, currency_imag, home_imag, send_money_imag, settings_imag = self.load_and_create_image()

        self.left_frame_build(account_imag, currency_imag, home_imag, settings_imag)

        self.center_home_build(add_money_imag, send_money_imag)

        right_left = tk.CTkLabel(master=right_frame, text="RL", corner_radius=10)
        right_left.pack(pady=12, padx=10, side=tk.LEFT)
        right_center = tk.CTkLabel(master=right_frame, text="RC", corner_radius=10)
        right_center.pack(pady=12, padx=10, side=tk.BOTTOM)
        right_right = tk.CTkLabel(master=right_frame, text="RR", corner_radius=10)
        right_right.pack(pady=12, padx=10, side=tk.RIGHT)

        # Uruchom pętlę główną nowego okna
        app_window.mainloop()

    def load_and_create_image(self):
        home_white_image = Image.open("images/outline_home_black_48dp.png")
        home_black_image = Image.open("images/outline_home_white_48dp.png")
        account_white_image = Image.open("images/outline_account_balance_black_48dp.png")
        account_black_image = Image.open("images/outline_account_balance_white_48dp.png")
        currency_white_image = Image.open("images/outline_currency_exchange_black_48dp.png")
        currency_black_image = Image.open("images/outline_currency_exchange_white_48dp.png")
        settings_white_image = Image.open("images/outline_manage_accounts_black_48dp.png")
        settings_black_image = Image.open("images/outline_manage_accounts_white_48dp.png")
        add_money_black_image = Image.open("images/outline_add_black_48dp.png")
        add_money_white_image = Image.open("images/outline_add_white_48dp.png")
        send_money_black_image = Image.open("images/outline_send_black_48dp.png")
        send_money_white_image = Image.open("images/outline_send_white_48dp.png")
        # create image
        home_imag = tk.CTkImage(light_image=home_white_image,
                                dark_image=home_black_image)
        account_imag = tk.CTkImage(light_image=account_white_image,
                                   dark_image=account_black_image)
        currency_imag = tk.CTkImage(light_image=currency_white_image,
                                    dark_image=currency_black_image)
        settings_imag = tk.CTkImage(light_image=settings_white_image,
                                    dark_image=settings_black_image)
        self.add_money_imag = tk.CTkImage(light_image=add_money_white_image,
                                          dark_image=add_money_black_image)
        self.send_money_imag = tk.CTkImage(light_image=send_money_white_image,
                                           dark_image=send_money_black_image)
        return account_imag, self.add_money_imag, currency_imag, home_imag, self.send_money_imag, settings_imag

    def left_frame_build(self, account_imag, currency_imag, home_imag, settings_imag):
        # add image to left frame
        home_control_label = tk.CTkLabel(master=self.left_frame, image=home_imag, text="   Home  ", compound=tk.LEFT,
                                         font=('Noto Sans', 20),
                                         text_color="white")
        home_control_label.pack(pady=(220, 12), padx=10, side=tk.TOP)
        account_control_label = tk.CTkLabel(master=self.left_frame, image=account_imag, text="   My Account  ",
                                            compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        account_control_label.pack(pady=12, padx=10, side=tk.TOP)
        currency_control_label = tk.CTkLabel(master=self.left_frame, image=currency_imag, text="   Currency  ",
                                             compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        currency_control_label.pack(pady=12, padx=10, side=tk.TOP)
        settings_control_label = tk.CTkLabel(master=self.left_frame, image=settings_imag, text="   Settings  ",
                                             compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        settings_control_label.pack(pady=12, padx=10, side=tk.TOP)

        # SET CURSOR ON MENU LABELS
        home_control_label.configure(cursor="hand2")
        account_control_label.configure(cursor="hand2")
        currency_control_label.configure(cursor="hand2")
        settings_control_label.configure(cursor="hand2")

        # HOVER EFFECTS
        home_control_label.bind("<Enter>", lambda event: home_control_label.configure(text_color="red",
                                                                                      font=('Noto Sans', 21, 'bold')))
        home_control_label.bind("<Leave>",
                                lambda event: home_control_label.configure(text_color="white", font=('Noto Sans', 20)))
        account_control_label.bind("<Enter>", lambda event: account_control_label.configure(text_color="red", font=(
            'Noto Sans', 21, 'bold')))
        account_control_label.bind("<Leave>", lambda event: account_control_label.configure(text_color="white",
                                                                                            font=('Noto Sans', 20)))
        currency_control_label.bind("<Enter>", lambda event: currency_control_label.configure(text_color="red", font=(
            'Noto Sans', 21, 'bold')))
        currency_control_label.bind("<Leave>", lambda event: currency_control_label.configure(text_color="white",
                                                                                              font=('Noto Sans', 20)))
        settings_control_label.bind("<Enter>", lambda event: settings_control_label.configure(text_color="red", font=(
            'Noto Sans', 21, 'bold')))
        settings_control_label.bind("<Leave>", lambda event: settings_control_label.configure(text_color="white",
                                                                                              font=('Noto Sans', 20)))

        # BINDING EVENTS
        home_control_label.bind("<Button-1>", lambda event: self.center_home_build(
            self.add_money_imag, self.send_money_imag))

        currency_control_label.bind("<Button-1>", lambda event: self.currency_center_build(
            self.center_frame))

        settings_control_label.bind("<Button-1>", lambda event: self.settings_center_build(
            self.center_frame))

        # delete widgets in center frame
        account_control_label.bind("<Button-1>", lambda event: self.clear_center_frame())

    def add_money_frame(self):
        print("Add money")
        # Create a new window
        add_money_window = tk.CTk()
        add_money_window.geometry("400x300")
        add_money_window.title("Add Money")
        add_money_window.configure(fg_color=self.my_colors.get("grey_blue_color"))

        # Create a label
        add_money_label = tk.CTkLabel(master=add_money_window, text="Deposit Money", font=("Noto Sans", 22, "bold"),
                                        text_color="black")
        add_money_label.pack(pady=10, padx=10)

        # Create an entry widget
        amount_entry = tk.CTkEntry(master=add_money_window, font=("Noto Sans", 20), fg_color="black", bg_color="white")
        amount_entry.pack(pady=10, padx=10)

        # Choose currency
        currency_label = tk.CTkLabel(master=add_money_window, text="Choose currency", font=("Noto Sans", 22, "bold"),
                                        text_color="black")
        currency_label.pack(pady=10, padx=10)

        list_of_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'RUB']
        # Add entry widget
        currency_option_menu = tk.CTkOptionMenu(master=add_money_window, values=list_of_currencies, font=("Noto Sans", 20),
                                                     fg_color=self.my_colors["sky_blue_color"], bg_color=self.my_colors["light_grey_color"])
        currency_option_menu.pack(pady=2, padx=10)


        # Button
        deposit_button = tk.CTkButton(master=add_money_window, text="Deposit", font=("Noto Sans", 22, "bold"),
                                        fg_color=self.my_colors["dark_grey_color"],
                                        width=180, height=40)
        deposit_button.pack(pady=(5, 40), padx=10, side=tk.BOTTOM)

        # SET CURSOR ON BUTTONS
        deposit_button.configure(cursor="hand2")

        # BINDING EVENTS
        deposit_button.bind("<Button-1>", lambda event: self.deposit_money(amount_entry.get(), currency_option_menu.get()))

        # show the window
        add_money_window.mainloop()

    def center_home_build(self, add_money_imag, send_money_imag):
        # set new balance in user_info
        self.user_info["balance"] = self.fetch_user_balance(self.username)
        self.user_info["transactions"] = self.fetch_user_transactions(self.username)

        # Calculate heights based on percentages
        welcome_height = 0.10
        balance_height = 0.10
        operation_height = 0.25
        history_height = 0.45
        rest_height = 0.10
        # Welcome Area
        welcome_area = tk.CTkFrame(master=self.center_frame)
        welcome_area.place(relwidth=1.0, relheight=welcome_height, relx=0, rely=0)
        welcome_area.configure(fg_color=self.my_colors.get("light_grey_color"))
        welcome_label = tk.CTkLabel(master=welcome_area, text=f'Welcome {self.username}', text_color='black',
                                    font=('Noto Sans', 34))
        welcome_label.pack(pady=12, padx=30, side=tk.LEFT)

        # Balance Area

        # Get data about user
        user_main_currency = self.user_info.get("main_currency")
        print(f'User main {user_main_currency}')
        # fetch balance of main currency
        user_balance = self.user_info.get("balance").get(user_main_currency)
        print(f'User balance: {user_balance}')


        balance_area = tk.CTkFrame(master=self.center_frame)
        balance_area.place(relwidth=1.0, relheight=balance_height, relx=0, rely=welcome_height)
        balance_area.configure(fg_color=self.my_colors.get("light_grey_color"))
        balance_label = tk.CTkLabel(master=balance_area, text=f'Account balance: {user_balance} {user_main_currency}'
                                    , text_color='black',
                                    font=('Noto Sans', 28))
        balance_label.pack(pady=20, padx=15, side=tk.BOTTOM)
        # account_balance.configure(text_color="red")



        # Operations Area
        operations_area = tk.CTkFrame(master=self.center_frame)
        operations_area.place(relwidth=1.0, relheight=operation_height, relx=0, rely=welcome_height + balance_height)
        operations_area.configure(fg_color=self.my_colors.get("light_grey_color"))
        add_money_button = tk.CTkButton(master=operations_area, width=200, height=50, image=add_money_imag,
                                        text="   Add Money  ",
                                        compound=tk.RIGHT, font=('Noto Sans', 22), text_color="black",
                                        border_color=self.my_colors.get("sky_blue_color"), border_width=2,
                                        fg_color=self.my_colors.get("light_grey_color"),
                                        hover_color=self.my_colors.get("grey_blue_color"))
        add_money_button.pack(pady=12, padx=(90, 5), side=tk.LEFT)
        add_money_button.configure(cursor="plus")
        send_money_button = tk.CTkButton(master=operations_area, width=200, height=50, image=send_money_imag,
                                         text="   Send Money  ",
                                         compound=tk.RIGHT, font=('Noto Sans', 22), text_color="black",
                                         border_color=self.my_colors.get("sky_blue_color"), border_width=2,
                                         fg_color=self.my_colors.get("light_grey_color"),
                                         hover_color=self.my_colors.get("grey_blue_color"))
        send_money_button.pack(pady=12, padx=(5, 90), side=tk.RIGHT)
        send_money_button.configure(cursor="plus")

        # BINDING EVENTS
        add_money_button.bind("<Button-1>", lambda event: self.add_money_frame())
        send_money_button.bind("<Button-1>", lambda event: self.send_money_window())


        # History Area
        history_area = tk.CTkFrame(master=self.center_frame)
        history_area.place(relwidth=1.0, relheight=history_height, relx=0,
                           rely=welcome_height + balance_height + operation_height)
        history_area.configure(fg_color=self.my_colors.get("light_grey_color"))
        # history_label = tk.CTkLabel(master=history_area, text="History", text_color='black', font=('Noto Sans', 28))
        # history_label.pack(pady=5, side=tk.TOP)
        history_main_info_label = tk.CTkLabel(master=history_area, text="Last 5 transactions:", text_color='black',
                                              font=('Noto Sans', 28))
        history_main_info_label.pack(pady=20, side=tk.TOP)
        # Sample values:
        value = [[]]
        # History Table
        transaction_table = CTkTable(master=history_area, column=5, row=6,
                                     header_color=self.my_colors.get("sky_blue_color"),
                                     values=value, hover=True, hover_color="green", width=700, height=1100)
        transaction_table.pack(pady=5, padx=5, side=tk.BOTTOM)
        transaction_table.insert(0, 0, "Date")
        transaction_table.insert(0, 1, "Type")
        transaction_table.insert(0, 2, "Amount")
        transaction_table.insert(0, 3, "Currency")
        transaction_table.insert(0, 4, "Status")
        # Add a sample record

        # Add transaction from user_info["transactions"]
        currency_dict = {
            1: "USD",
            2: "EUR",
            3: "GBP",
            4: "JPY",
            5: "CNY",
            6: "RUB"
        }
        # if transaction[3] > 0 then it is deposit, if transaction[3] < 0 then it is withdraw

        # Wykonuj ponizsza petle max 5 razy
        for i, transaction in enumerate(self.user_info["transactions"]):
            if i < 5:
                transaction_table.insert(i + 1, 0, transaction[2])
                transaction_table.insert(i + 1, 1, "Deposit" if transaction[3] > 0 else "Withdraw")
                transaction_table.insert(i + 1, 2, transaction[3])
                transaction_table.insert(i + 1, 3, currency_dict.get(transaction[4]))
                transaction_table.insert(i + 1, 4, "Completed")

        # transaction_table.insert(1, 0, "2021-01-01")
        # transaction_table.insert(1, 1, "Deposit")
        # transaction_table.insert(1, 2, "100")
        # transaction_table.insert(1, 3, "USD")
        # transaction_table.insert(1, 4, "Completed")
        # # Add a sample record
        # transaction_table.insert(2, 0, "2023-10-20")
        # transaction_table.insert(2, 1, "Withdraw")
        # transaction_table.insert(2, 2, "100")
        # transaction_table.insert(2, 3, "USD")
        # transaction_table.insert(2, 4, "Completed")
        # # Add a sample record
        # transaction_table.insert(3, 0, "2023-10-20")
        # transaction_table.insert(3, 1, "Withdraw")
        # transaction_table.insert(3, 2, "100")
        # transaction_table.insert(3, 3, "EUR")
        # transaction_table.insert(3, 4, "Completed")
        # # Add transfer record
        # transaction_table.insert(4, 0, "2023-10-27")
        # transaction_table.insert(4, 1, "Transfer")
        # transaction_table.insert(4, 2, "1230.33")
        # transaction_table.insert(4, 3, "USD")
        # transaction_table.insert(4, 4, "Completed")
        # Add transfer record

        # Rest Area
        rest_area = tk.CTkFrame(master=self.center_frame)
        rest_area.place(relwidth=1.0, relheight=rest_height, relx=0,
                        rely=welcome_height + balance_height + operation_height + history_height)
        rest_area.configure(fg_color=self.my_colors.get("light_grey_color"))

    def currency_center_build(self, center_frame):
        self.clear_center_frame()
        currency_frame = CurrencyFrame(self.center_frame, self.user_info)

    def settings_center_build(self, center_frame):
        self.clear_center_frame()
        settings_frame = SettingsFrame(self.center_frame, self.user_info)



    def clear_center_frame(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

    def deposit_money(self, amount, currency):

        # Find currency
        conn = sqlite3.connect('currency_exchange.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT id FROM currencies WHERE code = '{currency}'")
        currency_id = cursor.fetchone()[0]

        cursor.execute(f"SELECT id FROM users WHERE username = '{self.username}'")
        user_id = cursor.fetchone()[0]

        column_string = f'balance_{currency}'
        print(column_string)
        cursor.execute(f"SELECT {column_string} FROM accounts WHERE user_id = {user_id}")
        current_balance = cursor.fetchone()[0]

        new_balance = current_balance + float(amount)

        cursor.execute(f"UPDATE accounts SET {column_string} = {new_balance} WHERE user_id = {user_id}")
        conn.commit()

        # Add new transaction - Date format: YYYY-MM-DD
        cursor.execute(f"INSERT INTO transactions (id_account, date, amount, currency) "
                       f"VALUES ((SELECT id FROM accounts WHERE user_id = {user_id}), "
                       f"'{datetime.now().strftime('%Y-%m-%d')}', {amount}, {currency_id})")
        conn.commit()

        cursor.close()
        conn.close()

        # Wait for 1.5 seconds and do message box
        self.frame.after(1500, lambda: CTkMessagebox(title="Deposit", message=f"Deposited \n{amount} {currency}"))

    def fetch_user_transactions(self, username):
        conn = sqlite3.connect('currency_exchange.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
        user_id = cursor.fetchone()[0]

        cursor.execute(f"SELECT * FROM transactions WHERE id_account = (SELECT id FROM accounts WHERE user_id = {user_id})")
        transactions = cursor.fetchall()

        cursor.close()
        conn.close()

        print(transactions)

        for transaction in transactions:
            print(transaction)

        # sort transactions by date
        transactions = sorted(transactions, key=lambda x: datetime.strptime(x[2], '%Y-%m-%d'), reverse=True)

        return transactions



