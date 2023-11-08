import tkinter as tk
from tkinter import scrolledtext

import socket


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

        # set defaults
        # self.ip_var.set("10.61.1.42")
        # self.port_var.set("1555")
        # self.email_var.set("ahmetmelih@sabanciuniv.edu")
        # self.name_var.set("Ahmet Melih Afsar")

    def create_right_grid(self):
        right_frame = tk.Frame(self.root)
        right_frame.grid(row=0, column=1, padx=10, pady=10)

        self.output_box = scrolledtext.ScrolledText(right_frame, width=60, height=10)
        self.output_box.pack()

    def connect(self):
        ip = self.ip_var.get()
        port = self.port_var.get()
        email = self.email_var.get()
        name = self.name_var.get()

        # now we open socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((ip, int(port)))
        except:
            self.output_box.insert(tk.END, "Problem occurred while connecting...\n")
            return

        self.output_box.insert(tk.END, "Connection established...\n")

        # Send my email and full name
        msg_to_send = f"{email} {name}"
        self.socket.sendall(msg_to_send.encode())

        self.output_box.insert(tk.END, f"Message sent: {msg_to_send}\n")
        # receive data
        data = self.socket.recv(1024)

        # receive the data back to str
        token = data.decode()

        # print the received data into the screen
        self.output_box.insert(tk.END, f"Server: {token}\n")

        # now we will calculate answer to the server
        # by using the digits of token in a circular way to shift chars in the email string
        # and send it back to the server

        # first we will shift the chars in the email string
        # by using token
        shifted_email = ""
        for i in range(len(email)):
            shifted_email += chr(ord(email[i]) + int(token[i % len(token)]))

        # sum up the ascii values of each character in
        # the shifted string and send the resulting integer value

        my_sum = 0
        for char in shifted_email:
            my_sum += ord(char)

        self.socket.sendall(f"{str(my_sum)} {name}".encode())
        self.output_box.insert(tk.END, f"Message sent: {str(my_sum)} {name}\n")

        data2 = self.socket.recv(1024)

        self.output_box.insert(tk.END, f"Server: {data2.decode()}\n")

    def run(self):
        self.root.mainloop()
