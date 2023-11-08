import tkinter as tk
from tkinter import scrolledtext

class UI:
    def __init__(self, root):
        self.root = root
        self.create_left_grid()
        self.create_right_grid()

    def create_left_grid(self):
        left_frame = tk.Frame(self.root)
        left_frame.grid(row=0, column=0, padx=10, pady=10)

        self.ip_var = tk.StringVar()
        self.port_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.name_var = tk.StringVar()

        ip_label = tk.Label(left_frame, text="IP:")
        ip_label.grid(row=0, column=0, padx=10, pady=10)
        ip_entry = tk.Entry(left_frame, textvariable=self.ip_var)
        ip_entry.grid(row=0, column=1, padx=10, pady=10)

        port_label = tk.Label(left_frame, text="Port:")
        port_label.grid(row=1, column=0, padx=10, pady=10)
        port_entry = tk.Entry(left_frame, textvariable=self.port_var)
        port_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = tk.Label(left_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(left_frame, textvariable=self.email_var)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        name_label = tk.Label(left_frame, text="Name:")
        name_label.grid(row=3, column=0, padx=10, pady=10)
        name_entry = tk.Entry(left_frame, textvariable=self.name_var)
        name_entry.grid(row=3, column=1, padx=10, pady=10)

        connect_button = tk.Button(left_frame, text="Connect", command=self.connect)
        connect_button.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

    def create_right_grid(self):
        right_frame = tk.Frame(self.root)
        right_frame.grid(row=0, column=1, padx=10, pady=10)

        self.output_box = scrolledtext.ScrolledText(right_frame, width=30, height=10)
        self.output_box.pack()

    def connect(self):
        ip = self.ip_var.get()
        port = self.port_var.get()
        msg = self.email_var.get()

        # Call the function to connect here
        # For now, it just prints the inputs to the output box
        self.output_box.insert(tk.END, f"IP: {ip}\nPort: {port}\nMessage: {msg}\n")

    def run(self):
        self.root.mainloop()