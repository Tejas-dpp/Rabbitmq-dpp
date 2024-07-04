from nameko.rpc import rpc, RpcProxy

class PublisherService:
    name = "publisher"

    listener = RpcProxy('listener')

    @rpc
    def publish_message(self, message):
        print(f"Publishing message: {message}")
        self.listener.receive_message(message)
        return message
