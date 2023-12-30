import customtkinter as tk


class AppView:
    def __init__(self):
        self.master = tk.CTk()
        self.setup_applications_widgets()

    def destroy_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def setup_applications_widgets(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Podział ekranu na trzy części: 15%, 55%, 30%
        width_15_percent = int(0.15 * screen_width)
        width_55_percent = int(0.55 * screen_width)
        width_30_percent = int(0.30 * screen_width)


        width_90_percent = int(0.90 * screen_width)
        height_90_percent = int(0.90 * screen_height)
        # Utworzenie nowego okna CTk
        app_window = tk.CTk()

        # 90% wysokości ekranu and 90% szerokości ekranu
        #app_window.geometry(f"{width_90_percent}x{height_90_percent}")
        app_window.geometry("1280x720")
        # Utworzenie trzech obszarów z odpowiednimi szerokościami
        left_frame = tk.CTkFrame(master=app_window)
        left_frame.place(relwidth=0.15, relheight=1.0, relx=0, rely=0)

        center_frame = tk.CTkFrame(master=app_window)
        center_frame.place(relwidth=0.55, relheight=1.0, relx=0.15, rely=0)

        right_frame = tk.CTkFrame(master=app_window)
        right_frame.place(relwidth=0.30, relheight=1.0, relx=0.70, rely=0)

        # Dodaj dowolne widgety do każdego obszaru
        label_left = tk.CTkLabel(master=left_frame, text="Left Frame", corner_radius=10)
        label_left.pack(pady=12, padx=10)

        label_center = tk.CTkLabel(master=center_frame, text="Center Frame", corner_radius=10)
        label_center.pack(pady=12, padx=10)

        label_right = tk.CTkLabel(master=right_frame, text="Right Frame", corner_radius=10)
        label_right.pack(pady=12, padx=10)

        label_new = tk.CTkLabel(master=right_frame, text="Rigdsaht Frame", corner_radius=10)
        label_new.pack(pady=12, padx=10, side=tk.BOTTOM)

        label_new = tk.CTkLabel(master=right_frame, text="Rigdsaht Frame", corner_radius=10)
        label_new.pack(pady=12, padx=10, side=tk.LEFT)
        # Uruchom pętlę główną nowego okna
        app_window.mainloop()

