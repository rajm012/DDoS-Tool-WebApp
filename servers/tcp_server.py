# tcp_server.py
import socket

def start_tcp_server(ip="0.0.0.0", port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(5)
    print(f"TCP server listening on {ip}:{port}")

    while True:
        client, addr = sock.accept()
        print(f"Connection from {addr}")
        client.close()

if __name__ == "__main__":
    start_tcp_server()