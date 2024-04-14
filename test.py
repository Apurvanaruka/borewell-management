import tkinter as tk

class TrainInput(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

        # Add some train times to the listbox
        self.listbox.insert(tk.END, "10:00 AM")
        self.listbox.insert(tk.END, "11:00 AM")
        self.listbox.insert(tk.END, "12:00 PM")

        # Get the selected train time
        self.selected_time = self.listbox.get(tk.ACTIVE)

        # Create a button to submit the selected time
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        # Get the selected train time
        self.selected_time = self.listbox.get(tk.ACTIVE)

        # Print the selected train time to the console
        print(self.selected_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainInput(root)
    app.pack()
    root.mainloop()
