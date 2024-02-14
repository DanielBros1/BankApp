import customtkinter as tk
from PIL import ImageTk, Image
from CTkTable import *

from views.currency_frame import CurrencyFrame


class AppView:
    def __init__(self, frame):
        self.frame = frame
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
        self.setup_applications_widgets()

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

        # delete widgets in center frame
        account_control_label.bind("<Button-1>", lambda event: self.clear_center_frame())

    def center_home_build(self, add_money_imag, send_money_imag):
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
        welcome_label = tk.CTkLabel(master=welcome_area, text="Welcome UserName", text_color='black',
                                    font=('Noto Sans', 34))
        welcome_label.pack(pady=12, padx=30, side=tk.LEFT)
        # Balance Area
        balance_area = tk.CTkFrame(master=self.center_frame)
        balance_area.place(relwidth=1.0, relheight=balance_height, relx=0, rely=welcome_height)
        balance_area.configure(fg_color=self.my_colors.get("light_grey_color"))
        your_balance = "$10,200.54"
        balance_label = tk.CTkLabel(master=balance_area, text=f'Account Balance {your_balance}', text_color='black',
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
        value = [[1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5]]
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
        transaction_table.insert(1, 0, "2021-01-01")
        transaction_table.insert(1, 1, "Deposit")
        transaction_table.insert(1, 2, "100")
        transaction_table.insert(1, 3, "USD")
        transaction_table.insert(1, 4, "Completed")
        # Add a sample record
        transaction_table.insert(2, 0, "2023-10-20")
        transaction_table.insert(2, 1, "Withdraw")
        transaction_table.insert(2, 2, "100")
        transaction_table.insert(2, 3, "USD")
        transaction_table.insert(2, 4, "Completed")
        # Add a sample record
        transaction_table.insert(3, 0, "2023-10-20")
        transaction_table.insert(3, 1, "Withdraw")
        transaction_table.insert(3, 2, "100")
        transaction_table.insert(3, 3, "EUR")
        transaction_table.insert(3, 4, "Completed")
        # Add transfer record
        transaction_table.insert(4, 0, "2023-10-27")
        transaction_table.insert(4, 1, "Transfer")
        transaction_table.insert(4, 2, "1230.33")
        transaction_table.insert(4, 3, "USD")
        transaction_table.insert(4, 4, "Completed")
        # Add transfer record
        transaction_table.insert(5, 0, "2023-10-27")
        transaction_table.insert(5, 1, "Transfer")
        transaction_table.insert(5, 2, "1230.33")
        transaction_table.insert(5, 3, "USD")
        transaction_table.insert(5, 4, "Completed")
        # Rest Area
        rest_area = tk.CTkFrame(master=self.center_frame)
        rest_area.place(relwidth=1.0, relheight=rest_height, relx=0,
                        rely=welcome_height + balance_height + operation_height + history_height)
        rest_area.configure(fg_color=self.my_colors.get("light_grey_color"))

    def currency_center_build(self, center_frame):
        self.clear_center_frame()
        currency_frame = CurrencyFrame(self.center_frame)

    def clear_center_frame(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy()
