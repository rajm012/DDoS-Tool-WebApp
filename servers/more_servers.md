1. For Slowloris use tcp or this

- python -m http.server 8000

2. For DNS Amplification

- You can use a DNS server like dnsmasq or bind9 to test DNS amplification


Attack Type	Server Type	How to Set Up
UDP Flood	UDP Server	Use the udp_server.py script provided above.
SYN Flood	TCP Server	Use the tcp_server.py script provided above.
ICMP Flood	ICMP Monitor	Use Wireshark or tcpdump to monitor ICMP traffic.
Slowloris	HTTP Server	Use python -m http.server 8000.
DNS Amplification	DNS Server	Use dnsmasq or bind9 to set up a DNS server.