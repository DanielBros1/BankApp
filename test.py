import customtkinter as tk

# File to test functionalities
class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x100")
        self.frame = tk.CTkFrame(master=self.master)
        self.frame.pack(padx=15, pady=20, fill=tk.BOTH, expand=True)

        # Create a horizontal progress bar
        self.progressbar = tk.CTkProgressBar(self.frame, orientation="horizontal", width=300, height=20)
        self.progressbar.pack(pady=20)

        # Configure progress bar
        self.progressbar.configure(mode="determinate")

        # Automatically start loading when the application is initialized
        self.start_loading()

    def start_loading(self):
        # Reset progress bar
        self.progressbar.set(0)

        # Simulate loading for 5 seconds
        self.loading_process(0.01, 5)

    def loading_process(self, step, duration):
        current_value = 0
        total_steps = int(duration / step)

        def update_progress():
            nonlocal current_value
            if current_value < total_steps:
                # Update progress bar
                current_value += 1
                self.progressbar.set(current_value / total_steps)

                # Schedule the next update
                self.frame.after(int(step * 1000), update_progress)
            else:
                # Reset progress bar when loading is complete
                self.progressbar.set(1.0)

        # Start the loading process
        update_progress()


if __name__ == "__main__":
    root = tk.CTk()
    app = MyApp(root)
    root.mainloop()