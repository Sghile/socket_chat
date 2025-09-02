import socket
import threading
from abc import ABC, abstractmethod


class SocketConnection:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_and_listen(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def accept(self):
        return self.sock.accept()

    def connect(self):
        self.sock.connect((self.host, self.port))

    def send(self, conn, msg: str):
        conn.sendall(msg.encode())

    def receive(self, conn, bufsize=1024) -> str:
        return conn.recv(bufsize).decode()


class ChatParticipant(ABC):
    def __init__(self, connection: SocketConnection):
        self.connection = connection

    @abstractmethod
    def start(self):
        pass

    def start_threads(self, send_func, recv_func):
        threading.Thread(target=recv_func, daemon=True).start()
        threading.Thread(target=send_func, daemon=True).start()
        threading.Event().wait()
