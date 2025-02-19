from time import sleep
from channels.consumer import SyncConsumer


class PingConsumer(SyncConsumer):
    def websocket_connect(self, message):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, message):
        sleep(1)
        self.send({
            "type": "websocket.send",
            "text": "pong",
        })
