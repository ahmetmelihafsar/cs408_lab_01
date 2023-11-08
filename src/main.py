import tkinter as tk
from ui import UI
from network import Network

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.ui = UI(self.root)
        self.network = Network()

    def connect(self):
        ip = self.ui.get_ip()
        port = self.ui.get_port()
        message = self.ui.get_message()
        output = self.network.connect(ip, port, message)
        self.ui.display_output(output)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()