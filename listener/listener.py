from nameko.rpc import rpc
import logging

logging.basicConfig(level=logging.INFO)

class ListenerService:
    name = "listener"

    @rpc
    def receive_message(self, message):
        logging.info(f"Received message: {message}")
        print(f"Received message: {message}")
