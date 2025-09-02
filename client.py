from base import SocketConnection, ChatParticipant


class ChatClient(ChatParticipant):

    def start(self):
        self.connection.connect()
        print(f"Connected to {self.connection.host}:{self.connection.port}")

        def receive():
            while True:
                msg = self.connection.receive(self.connection.sock)
                if not msg:
                    break
                print(f"\nServer: {msg}")

        def send():
            while True:
                msg = input("Message: ")
                self.connection.send(self.connection.sock, msg)

        self.start_threads(send, receive)


if __name__ == "__main__":
    client = ChatClient(SocketConnection("127.0.0.1", 5000))
    client.start()
