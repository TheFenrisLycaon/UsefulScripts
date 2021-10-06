import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import socket
import threading

kivy.require("1.9.0")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def sendMessage(self):
        client.send(
            f"{self.username_text.text} ::\t{self.message_text.text}".encode('utf-8'))

    def connectToServer(self):
        if self.username_text != "":
            client.connect((self.ip_text.text, 9999))
            message = client.recv(1024).decode('utf-8')
            if message == "Username:":
                client.send(self.username_text.text.encode('utf-8'))
                self.send_btn.disabled = 0
                self.message_text.disabled = 0
                self.connect_btn.disabled = 1
                self.ip_text.disabled = 1

                self.makeInvisible(self.connection_grid)
                self.makeInvisible(self.connection_grid)

                thread = threading.Thread(target=self.receive)
                thread.start()

    def makeInvisible(self, widget):
        widget.visible = 0
        widget.size_hint_x = None
        widget.size_hint_y = None
        widget.height = 0
        widget.width = 0
        widget.text = ""
        widget.opacity = 0

    def receive(self):
        stop = 0
        while not stop:
            try:
                message = client.recv(1024).decode('utf-8')
                self.chat_text += message + "\n"
            except Exception as e:
                print(e)
                client.close()
                stop = 1


class WebChat(App):

    def build(self):
        return MyRoot()


webChat = WebChat()
webChat.run()
