# DDoS Tool 🚀

A powerful and ethical DDoS testing tool designed for security professionals and developers to simulate and analyze various types of DDoS attacks. This tool helps you understand how attacks work and how to defend against them.


---

## Features ✨

- **Multiple Attack Types**: Simulate UDP Flood, SYN Flood, HTTP Flood, ICMP Flood, Slowloris, and DNS Amplification attacks.
- **User-Friendly Interface**: Easy-to-use web interface for configuring and launching attacks.
- **Real-Time Logs**: View attack logs and statistics in real-time.
- **Ethical Use Only**: Designed for educational and testing purposes only.
- **Cross-Platform**: Works on macOS, Linux, and other Unix-based systems.

---

## Table of Contents 📚

1. [Installation](#installation)
2. [Usage](#usage)
3. [Attack Types](#attack-types)
4. [Testing and Monitoring](#testing-and-monitoring)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation 🛠️

### Prerequisites
- Python 3.7 or higher
- Flask (`pip install flask`)
- Wireshark (optional, for network monitoring)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rajm012/ddos-tool.git
   cd ddos-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the tool in your browser:
   ```
   http://localhost:5000
   ```

---

## Usage 🖥️

1. **Home Page**: Navigate to the dashboard to view options.
2. **Start Attack**: Select an attack type, enter target details, and launch the attack.
3. **View Logs**: Monitor real-time attack logs and statistics.
4. **Help**: Click the floating help button (`?`) for detailed instructions on using the tool.

---

## Attack Types 💥

| Attack Type          | Description                                                                 | Input Values                                                                 |
|----------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **UDP Flood**        | Floods the target with UDP packets.                                         | Target IPs, Target Port, Duration, Intensity, Packet Size                   |
| **SYN Flood**        | Overwhelms the target with SYN requests.                                    | Target IPs, Target Port, Duration, Intensity                                |
| **HTTP Flood**       | Floods the target with HTTP requests.                                       | Target IPs, Target Port, Duration, Intensity, Custom Headers                |
| **ICMP Flood**       | Floods the target with ICMP (ping) packets.                                 | Target IPs, Duration, Intensity                                             |
| **Slowloris**        | Sends partial HTTP requests to exhaust the target's resources.              | Target IPs, Target Port, Duration, Intensity                                |
| **DNS Amplification**| Exploits DNS servers to flood the target with amplified traffic.            | Target IPs, Duration, Intensity                                             |

---

## Testing and Monitoring 🔍

### Tools for Testing
- **Wireshark**: Monitor network traffic and analyze packets.
- **Terminal**: View real-time logs and output directly in the terminal.
- **Logs Page**: Access detailed attack logs and statistics on the web interface.

### Example Commands
- Monitor UDP traffic with Wireshark:
  ```bash
  wireshark -k -i <interface> -f "udp"
  ```
- Check ICMP traffic:
  ```bash
  sudo tcpdump -i <interface> icmp
  ```

---

## Server Config 🌎

For every tool we can make our own server and i used two of the prominent methods:

1. Using inbuilt flask server as:
   ```bash
   python -m http.server 8000
   ```

2. Using the python script to make one server
   
   See the folder Servers where i have designed Snippet to get the various servers for testing. You can run that too to make a server on port 8000 and test it accoordingly.

---

## Contributing 🤝

We welcome contributions! Here’s how you can help:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License 📜

This project is licensed under the **MIT License**.  
*Please use this tool responsibly and only for ethical purposes.*

---

## Screenshots 📸

Visit Screenshot folder to see the screenshots of the tool.

---

## Support ❤️

If you find this project useful, please consider giving it a ⭐️ on GitHub!  
For questions or issues, open an issue on the [GitHub repository](https://github.com/rajm012/ddos-tool).

---

**Disclaimer**: This tool is intended for educational and testing purposes only. Do not use it for malicious activities. The developers are not responsible for any misuse of this tool.

---
