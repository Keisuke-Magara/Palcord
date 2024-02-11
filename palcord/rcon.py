import socket
import asyncio

# Only support localhost
class RCONClient:
    def __init__(self, port) -> None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.)
    
    async def send_command(self, cmd: str):
        ...

    def add_callback_on_listen(self, callback):
        ...
    
    async def __connect()