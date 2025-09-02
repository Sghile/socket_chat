from base import SocketConnection, ChatParticipant


class ChatServer(ChatParticipant):

    def start(self):
        self.connection.bind_and_listen()
        print(f"Server started {self.connection.host}:{self.connection.port}, member waiting for connection...")

        conn, addr = self.connection.accept()
        print(f"Client is connected: {addr}")

        def receive():
            while True:
                msg = self.connection.receive(conn)
                if not msg:
                    break
                print(f"\nClient: {msg}")

        def send():
            while True:
                msg = input("Message: ")
                self.connection.send(conn, msg)

        self.start_threads(send, receive)


if __name__ == "__main__":
    server = ChatServer(SocketConnection("0.0.0.0", 5000))
    server.start()
