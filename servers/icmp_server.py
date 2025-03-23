# icmp_server.py
import socket
import struct

def start_icmp_server():
    # Create a raw socket to capture ICMP packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    print("ICMP server listening for echo requests...")

    while True:
        packet, addr = sock.recvfrom(1024)
        # Extract the ICMP header (first 8 bytes)
        icmp_header = packet[20:28]
        icmp_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", icmp_header)
        if icmp_type == 8:  # ICMP echo request
            print(f"Received ICMP echo request from {addr}")

if __name__ == "__main__":
    start_icmp_server()

    