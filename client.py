import socket
import threading


class Client:

    def __init__(self, host="127.0.0.1", port=5000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host, self.port = host, port

    def receive_loop(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                print(f"[SERVER]: {data.decode()}")
            except ConnectionResetError:
                print("[CLIENT] Disconnected.")
                break

    def send_loop(self):
        while True:
            self.sock.send(input().encode())

    def start(self):
        self.sock.connect((self.host, self.port))
        print(f"[CLIENT] Connected {self.host}:{self.port}")
        threading.Thread(target=self.receive_loop, daemon=True).start()
        self.send_loop()


if __name__ == "__main__":
    Client().start()
