
import socket
class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port, message):
        self.socket.connect((ip, port))
        self.socket.sendall(message.encode())
        data = self.socket.recv(1024)
        self.socket.close()
        return data.decode()
    
    