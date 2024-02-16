import customtkinter as tk
import re
import sqlite3

from app_view import AppView
from CTkMessagebox import CTkMessagebox

class BaseView:
    def __init__(self, frame):
        self.frame = frame
        self.widgets = {}
        self.all_users = None
        self.connect_to_database()

    def destroy_widgets(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def connect_to_database(self):
        # Connect to database
        conn = sqlite3.connect("currency_exchange.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users""")

        self.all_users = cursor.fetchall()
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        conn.close()
class RegisterView(BaseView):
    def __init__(self, frame):
        super().__init__(frame)
        self.destroy_widgets()

        self.connect_to_database()
        self.setup_registration_widgets()

    def setup_registration_widgets(self):

        # BUILDING WIDGETS
        register_label = tk.CTkLabel(master=self.frame, text="Registration", corner_radius=10, font=("Roboto", 30))
        register_label.pack(pady=12, padx=10)
        username_entry = tk.CTkEntry(master=self.frame, placeholder_text="Username", placeholder_text_color="grey",
                                     font=("Roboto", 14), height=36, width=150)
        username_entry.pack(pady=8, padx=10)
        first_name_entry = tk.CTkEntry(master=self.frame, placeholder_text="First Name", placeholder_text_color="grey",
                                       font=("Roboto", 14), height=36, width=150)
        last_name_entry = tk.CTkEntry(master=self.frame, placeholder_text="Last Name", placeholder_text_color="grey",
                                      font=("Roboto", 14), height=36, width=150)
        password_entry = tk.CTkEntry(master=self.frame, placeholder_text="Password", placeholder_text_color="grey",
                                     font=("Roboto", 14), height=36, width=150, show="*")
        confirm_password_entry = tk.CTkEntry(master=self.frame, placeholder_text="Confirm Password",
                                             placeholder_text_color="grey",
                                             font=("Roboto", 14), height=36, width=150, show="*")

        register_button = tk.CTkButton(master=self.frame, text="Register", font=("Roboto", 15),
                                       command=lambda: self.register(username=username_entry.get(),
                                                                     first_name=first_name_entry.get(),
                                                                     last_name=last_name_entry.get(),
                                                                     password=password_entry.get(),
                                                                     confirm_password=confirm_password_entry.get()))
        have_account_label = tk.CTkLabel(master=self.frame, text="Already have an account?", corner_radius=10)
        move_to_login_label = tk.CTkLabel(master=self.frame, text="Login here!", corner_radius=10, font=("Roboto", 17),
                                          text_color="cyan")

        self.password_empty_label = tk.CTkLabel(master=self.frame, corner_radius=10, text_color="red")

        # ADD WIDGETS TO DICTIONARY
        self.widgets["register_label"] = register_label
        self.widgets["username_entry"] = username_entry
        self.widgets["first_name_entry"] = first_name_entry
        self.widgets["last_name_entry"] = last_name_entry
        self.widgets["password_entry"] = password_entry
        self.widgets["confirm_password_entry"] = confirm_password_entry
        self.widgets["register_button"] = register_button
        self.widgets["have_account_label"] = have_account_label
        self.widgets["move_to_login_label"] = move_to_login_label
        self.widgets["password_empty_label"] = self.password_empty_label

        # NAMING WIDGETS

        register_label.widgetName = "register_label"
        username_entry.widgetName = "username_entry"
        first_name_entry.widgetName = "first_name_entry"
        last_name_entry.widgetName = "last_name_entry"
        password_entry.widgetName = "password_entry"
        confirm_password_entry.widgetName = "confirm_password_entry"
        register_button.widgetName = "register_button"
        have_account_label.widgetName = "have_account_label"
        move_to_login_label.widgetName = "move_to_login_label"
        self.password_empty_label.widgetName = "password_empty_label"

        move_to_login_label.configure(cursor="hand2")

        # STYLING WIDGETS
        first_name_entry.pack(pady=8, padx=10)
        last_name_entry.pack(pady=8, padx=10)
        password_entry.pack(pady=8, padx=10)
        confirm_password_entry.pack(pady=8, padx=10)
        register_button.pack(pady=(12, 3), padx=5)
        have_account_label.pack(pady=(12, 0))
        move_to_login_label.pack()

        # BINDING WIDGETS
        move_to_login_label.bind(sequence="<Button-1>", command=lambda event: self.login())

    def is_input_valid(self, username, first_name, last_name, password, confirm_password):
        # if any field is empty
        if username == "" or first_name == "" or last_name == "" or password == "" or confirm_password == "":
            CTkMessagebox(title="Error", message="All fields are required", icon="cancel", master=self.frame)
            return False

        # if username is less than 3 characters
        if len(username) < 3:
            CTkMessagebox(title="Error", message="Username must contain at least 3 characters", icon="cancel",
                          master=self.frame)
            return False

        # if first name or last name is less than 2 characters
        if len(first_name) < 2:
            CTkMessagebox(title="Error", message="First name must contain at least 2 characters", icon="cancel",
                          master=self.frame)
            return False

        # if first name or last name is less than 2 characters
        if len(last_name) < 2:
            CTkMessagebox(title="Error", message="Last name must contain at least 2 characters", icon="cancel",
                          master=self.frame)
            return False

        return True
    def register(self, username, first_name, last_name, password, confirm_password):

        if self.is_input_valid(username, first_name, last_name, password, confirm_password) is False:
            return

        # Check if username is already in database
        for user in self.all_users:
            if user[1] == username:
                CTkMessagebox(title="Error", message="Username already exists", icon="cancel", master=self.frame)
                return

        if self.password_validation(password, confirm_password) is True:

            conn = sqlite3.connect("currency_exchange.db")
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users (username, first_name, last_name, password)
                VALUES (?, ?, ?, ?)""", (username, first_name, last_name, password))
            conn.commit()

            cursor.execute("""
                SELECT id FROM users WHERE username = ?""", (username,))
            user_id = cursor.fetchone()[0]

            # If we create new user, we need to create new account for him
            cursor.execute("""
                INSERT INTO accounts (user_id)
                VALUES (?)""", (user_id,))
            conn.commit()

            cursor.close()
            conn.close()
            msg = CTkMessagebox(title="Success", message="You have been registered", icon="check",
                                master=self.frame, option_1="Login now", option_2="Ok", option_focus=1)

            if msg.get() == "Login now":
                self.login()

        print("Password: ", password)
        print("Confirm Password: ", confirm_password)

    def login(self):
        print("Login")
        # delete all dictionary widgets
        for widget in self.widgets.values():
            widget.destroy()
        LoginView(frame=self.frame)

    def password_validation(self, password, confirm_password):
        print("Password: ", password)
        print("Confirm Password: ", confirm_password)

        print(self.password_empty_label.widgetName)
        print(self.password_empty_label.children.items())
        print(self.password_empty_label.winfo_id())
        print(self.password_empty_label.winfo_name())

        if password != confirm_password:
            self.password_empty_label.configure(text="Passwords does not match")
            self.password_empty_label.pack(pady=(5, 0))
            return False
        elif password == confirm_password and self.is_strong_password(password):
            self.password_empty_label.pack_forget()
            return True
        else:
            return False

    def is_strong_password(self, password):
        # check if password contains at least 1 number, 1 uppercase letter, 1 lowercase letter and min 8 characters

        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

        if pattern.match(password):
            print("Password is strong")
            return True
        else:

            self.password_empty_label.configure(text="Password is not strong\nPassword must contain at least 1 number, "
                                                     "1 uppercase letter, 1 lowercase letter and min 8 characters")
            self.password_empty_label.pack(pady=(5, 0))
            print("Password is not strong")
            return False


class LoginView(BaseView):
    def __init__(self, frame):
        super().__init__(frame)
        self.destroy_widgets()

        self.connect_to_database()

        login_label = tk.CTkLabel(master=self.frame, text="Login System", corner_radius=10, font=("Roboto", 30))
        login_label.pack(pady=12, padx=10)

        username_entry = tk.CTkEntry(master=self.frame, placeholder_text="Username", placeholder_text_color="grey",
                                     font=("Roboto", 14), height=36, width=150)
        username_entry.pack(pady=8, padx=10)

        password_entry = tk.CTkEntry(master=self.frame, placeholder_text="Password", placeholder_text_color="grey",
                                     font=("Roboto", 14), height=36, width=150, show="*")
        password_entry.pack(pady=8, padx=10)

        login_button = tk.CTkButton(master=self.frame, text="Login",
                                    command=lambda: self.login(username_entry.get(),
                                                               password_entry.get()), font=("Roboto", 15))
        login_button.pack(pady=(12, 3), padx=5)

        no_account_label = tk.CTkLabel(master=self.frame, text="Don't have an account?", corner_radius=10)
        no_account_label.pack(pady=(12, 0))

        move_to_register_label = tk.CTkLabel(master=self.frame, text="Sign up here!", corner_radius=10,
                                             font=("Roboto", 17),
                                             text_color="cyan")
        move_to_register_label.pack()
        move_to_register_label.bind(sequence="<Button-1>", command=lambda event: self.register())
        move_to_register_label.configure(cursor="hand2")

    def open_app_view(self, username):
        for widget in self.frame.winfo_children():
            widget.destroy()

        AppView(self.frame, username)


     #   label = tk.CTkLabel(master=self.frame, text="New Window", corner_radius=10, font=("Roboto", 30))
     #   label.pack(pady=12, padx=10)

      #  button = tk.CTkButton(master=self.frame, text="Back", command=lambda: self.__init__(self.frame),
           #                   font=("Roboto", 15))
      # button.pack(pady=(12, 3), padx=5)

    def login(self, username, password):
        print("Login")

        print("Username: ", username)
        print("Password: ", password)

        # Check if username and password are in database
        for user in self.all_users:
            print(user[1], user[4])
            if user[1] == username and user[4] == password:
                self.start_login_process(username)
                return
        CTkMessagebox(title="Error", message="Invalid username or password", icon="cancel",
                      master=self.frame)

    def start_login_process(self, username):
        # delete acutal frame
        self.destroy_widgets()
 #       self.frame.destroy()
    #    var = self.frame.master
   #     self.frame.master.geometry("1330x330")
        # add circle progress bar
        progress_bar = tk.CTkProgressBar(master=self.frame, width=200, height=15, orientation="horizontal")
        progress_bar.configure(require_redraw=True)
        progress_bar.pack(pady=12)

        # add label
        label = tk.CTkLabel(master=self.frame, text="Loading...", corner_radius=10, font=("Roboto", 30))
        label.pack(pady=12, padx=10)

        self.start_loading(progress_bar, username)
      #  AppView()
        #self.open_new_window()

    def start_loading(self, progress_bar, username):
        # Reset progress bar
        progress_bar.set(0)

        # Simulate loading for 3 seconds
        self.loading_process(0.01, 0.01, progress_bar, username)

    def loading_process(self, step, duration, progress_bar, username):
        current_value = 0
        total_steps = int(duration / step)

        def update_progress():
            nonlocal current_value
            if current_value < total_steps:
                # Update progress bar
                current_value += 1
                progress_bar.set(current_value / total_steps)

                # Schedule the next update
                self.frame.after(int(step * 1000), update_progress)
            else:
                # Reset progress bar when loading is complete
                progress_bar.set(1.0)
                self.frame.after(1000, lambda: self.open_app_view(username))

        # Start the loading process
        update_progress()


    def register(self):
        print("Register")
        RegisterView(frame=self.frame)
