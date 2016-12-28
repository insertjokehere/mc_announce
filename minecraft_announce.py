import socket
import time
import os
from collections import namedtuple

Server = namedtuple('Server', ['name', 'port'])

servers = []

for e in os.environ:
    if e.startswith("MCSERVER_"):
        name = os.environ[e]
        port = int(e.split("_")[1])
        servers.append(Server(name, port))

BROADCAST_IP = "255.255.255.255"
BROADCAST_PORT = 4445

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("Broadcasting Minecraft servers to LAN")
for server in servers:
    print(" - {} (port {})".format(server.name, server.port))

while 1:
        for server in servers:
                msg = "[MOTD]%s[/MOTD][AD]%d[/AD]" % (server.name, server.port)
                sock.sendto(msg, (BROADCAST_IP, BROADCAST_PORT))
        time.sleep(1.5)
