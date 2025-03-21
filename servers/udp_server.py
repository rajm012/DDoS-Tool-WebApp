import socket

def start_udp_server(ip="0.0.0.0", port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"UDP server listening on {ip}:{port}")

    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received UDP packet from {addr}: {data}")

if __name__ == "__main__":
    start_udp_server()