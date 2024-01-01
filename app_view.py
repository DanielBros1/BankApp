import customtkinter as tk
from PIL import ImageTk, Image


class AppView:
    def __init__(self, frame):
        self.frame = frame
        self.setup_applications_widgets()

    def destroy_widgets(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def setup_applications_widgets(self):
        # DARK MODE
        dark_grey_color = "#2B2B2B"
        very_dark_grey_color = "#1E1E1E"
        some_dark_grey_color = "#4A4A4A"
        # LIGHT MODE
        light_grey_color = "#C9CDCD"
        sky_blue_color = "#4072F1"
        grey_blue_color = "#9FBBD2"


        app_window = self.frame.master
        app_window.geometry("1280x720")
        app_window.title("Banking App")


        # Utworzenie trzech obszarów z odpowiednimi szerokościami
        left_frame = tk.CTkFrame(master=app_window)
        left_frame.place(relwidth=0.15, relheight=1.0, relx=0, rely=0)
        #  left_frame.configure(fg_color=dark_grey_color)
        left_frame.configure(fg_color=sky_blue_color)
        left_frame.configure(cursor="mouse")

        center_frame = tk.CTkFrame(master=app_window)
        center_frame.place(relwidth=0.60, relheight=1.0, relx=0.15, rely=0)
        # center_frame.configure(fg_color=some_dark_grey_color)
        center_frame.configure(fg_color=light_grey_color)

        right_frame = tk.CTkFrame(master=app_window)
        right_frame.place(relwidth=0.25, relheight=1.0, relx=0.75, rely=0)
        # right_frame.configure(fg_color=very_dark_grey_color)
        right_frame.configure(fg_color=grey_blue_color)

        home_white_image = Image.open("outline_home_black_48dp.png")
        home_black_image = Image.open("outline_home_white_48dp.png")
        account_white_image = Image.open("outline_account_balance_black_48dp.png")
        account_black_image = Image.open("outline_account_balance_white_48dp.png")
        currency_white_image = Image.open("outline_currency_exchange_black_48dp.png")
        currency_black_image = Image.open("outline_currency_exchange_white_48dp.png")
        settings_white_image = Image.open("outline_manage_accounts_black_48dp.png")
        settings_black_image = Image.open("outline_manage_accounts_white_48dp.png")
        add_money_black_image = Image.open("outline_add_black_48dp.png")
        add_money_white_image = Image.open("outline_add_white_48dp.png")
        send_money_black_image = Image.open("outline_send_black_48dp.png")
        send_money_white_image = Image.open("outline_send_white_48dp.png")

        credit_card_three_image = Image.open("credit_card.jpg")
        card_3 = tk.CTkImage(light_image=credit_card_three_image, dark_image=credit_card_three_image, size=(300, 300))

        # create image
        home_imag = tk.CTkImage(light_image=home_white_image,
                                dark_image=home_black_image)

        account_imag = tk.CTkImage(light_image=account_white_image,
                                   dark_image=account_black_image)

        currency_imag = tk.CTkImage(light_image=currency_white_image,
                                    dark_image=currency_black_image)

        settings_imag = tk.CTkImage(light_image=settings_white_image,
                                    dark_image=settings_black_image)

        add_money_imag = tk.CTkImage(light_image=add_money_white_image,
                                     dark_image=add_money_black_image)

        send_money_imag = tk.CTkImage(light_image=send_money_white_image,
                                      dark_image=send_money_black_image)

        # add image to left frame
        h = tk.CTkLabel(master=left_frame, image=home_imag, text="   Home  ", compound=tk.LEFT, font=('Noto Sans', 20),
                        text_color="white")
        h.pack(pady=(220, 12), padx=10, side=tk.TOP)

        a = tk.CTkLabel(master=left_frame, image=account_imag, text="   My Account  ",
                        compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        a.pack(pady=12, padx=10, side=tk.TOP)

        c = tk.CTkLabel(master=left_frame, image=currency_imag, text="   Currency  ",
                        compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        c.pack(pady=12, padx=10, side=tk.TOP)

        s = tk.CTkLabel(master=left_frame, image=settings_imag, text="   Settings  ",
                        compound=tk.LEFT, font=('Noto Sans', 20), text_color="white")
        s.pack(pady=12, padx=10, side=tk.TOP)

        # SET CURSOR ON MENU LABELS
        h.configure(cursor="hand2")
        a.configure(cursor="hand2")
        c.configure(cursor="hand2")
        s.configure(cursor="hand2")

        # HOVER EFFECTS
        h.bind("<Enter>", lambda event: h.configure(text_color="red", font=('Noto Sans', 21, 'bold')))
        h.bind("<Leave>", lambda event: h.configure(text_color="white", font=('Noto Sans', 20)))
        a.bind("<Enter>", lambda event: a.configure(text_color="red", font=('Noto Sans', 21, 'bold')))
        a.bind("<Leave>", lambda event: a.configure(text_color="white", font=('Noto Sans', 20)))
        c.bind("<Enter>", lambda event: c.configure(text_color="red", font=('Noto Sans', 21, 'bold')))
        c.bind("<Leave>", lambda event: c.configure(text_color="white", font=('Noto Sans', 20)))
        s.bind("<Enter>", lambda event: s.configure(text_color="red", font=('Noto Sans', 21, 'bold')))
        s.bind("<Leave>", lambda event: s.configure(text_color="white", font=('Noto Sans', 20)))

        # Calculate heights based on percentages
        welcome_height = 0.10
        balance_height = 0.10
        operation_height = 0.25
        history_height = 0.35
        rest_height = 0.20

        # Welcome Area
        welcome_area = tk.CTkFrame(master=center_frame)
        welcome_area.place(relwidth=1.0, relheight=welcome_height, relx=0, rely=0)
        welcome_area.configure(fg_color=light_grey_color)

        welcome_label = tk.CTkLabel(master=welcome_area, text="Welcome UserName", text_color='black',
                                    font=('Noto Sans', 34))
        welcome_label.pack(pady=12, padx=30, side=tk.LEFT)

        # Balance Area
        balance_area = tk.CTkFrame(master=center_frame)
        balance_area.place(relwidth=1.0, relheight=balance_height, relx=0, rely=welcome_height)
        balance_area.configure(fg_color=light_grey_color)

        your_balance = "$10,200.54"

        balance_label = tk.CTkLabel(master=balance_area, text=f'Account Balance {your_balance}', text_color='black',
                                    font=('Noto Sans', 28))
        balance_label.pack(pady=20, padx=15, side=tk.BOTTOM)
        # account_balance.configure(text_color="red")

        # Operations Area
        operations_area = tk.CTkFrame(master=center_frame)
        operations_area.place(relwidth=1.0, relheight=operation_height, relx=0, rely=welcome_height + balance_height)
        operations_area.configure(fg_color=light_grey_color)

        add_money_button = tk.CTkButton(master=operations_area, width=200, height=50, image=add_money_imag,
                                        text="   Add Money  ",
                                        compound=tk.RIGHT, font=('Noto Sans', 22), text_color="black",
                                        border_color="blue", border_width=2, fg_color=light_grey_color,
                                        hover_color=grey_blue_color)

        add_money_button.pack(pady=12, padx=(90, 5), side=tk.LEFT)
        add_money_button.configure(cursor="plus")
        send_money_button = tk.CTkButton(master=operations_area, width=200, height=50, image=send_money_imag,
                                         text="   Send Money  ",
                                         compound=tk.RIGHT, font=('Noto Sans', 22), text_color="black",
                                         border_color="blue", border_width=2, fg_color=light_grey_color,
                                         hover_color=grey_blue_color)

        send_money_button.pack(pady=12, padx=(5, 90), side=tk.RIGHT)
        send_money_button.configure(cursor="plus")

        # History Area
        history_area = tk.CTkFrame(master=center_frame)
        history_area.place(relwidth=1.0, relheight=history_height, relx=0,
                           rely=welcome_height + balance_height + operation_height)
        history_area.configure(fg_color=light_grey_color)

        # Rest Area
        rest_area = tk.CTkFrame(master=center_frame)
        rest_area.place(relwidth=1.0, relheight=rest_height, relx=0,
                        rely=welcome_height + balance_height + operation_height + history_height)
        rest_area.configure(fg_color=light_grey_color)

        #
        # # Cards info
        # card_label = tk.CTkLabel(master=center_frame, text="Your Cards", text_color='black', font=('Noto Sans', 28))
        # card_label.pack(pady=5, side=tk.TOP)
        #
        # card_main_info_label = tk.CTkLabel(master=center_frame, text="Card ending in **** 1234", text_color='black', font=('Noto Sans', 28))
        # card_main_info_label.pack(pady=5, side=tk.TOP)
        #

        right_left = tk.CTkLabel(master=right_frame, text="RL", corner_radius=10)
        right_left.pack(pady=12, padx=10, side=tk.LEFT)
        right_center = tk.CTkLabel(master=right_frame, text="RC", corner_radius=10)
        right_center.pack(pady=12, padx=10, side=tk.BOTTOM)
        right_right = tk.CTkLabel(master=right_frame, text="RR", corner_radius=10)
        right_right.pack(pady=12, padx=10, side=tk.RIGHT)

        # Uruchom pętlę główną nowego okna
        app_window.mainloop()
