import socket
import threading


class Server:
    def __init__(self, host="0.0.0.0", port=5000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        print(f"[SERVER] waiting {host}:{port}...")
        self.conn, addr = self.sock.accept()
        print(f"[SERVER] connected: {addr}")

    def receive_loop(self):
        while True:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                print(f"[CLIENT]: {data.decode()}")
            except ConnectionResetError:
                print("[SERVER] disconnected.")
                break

    def send_loop(self):
        while True:
            self.conn.send(input().encode())

    def start(self):
        threading.Thread(target=self.receive_loop, daemon=True).start()
        self.send_loop()


if __name__ == "__main__":
    Server().start()
