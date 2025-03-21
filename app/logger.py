import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('config/attack_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  attack_type TEXT,
                  target_ip TEXT,
                  target_port INTEGER,
                  duration INTEGER,
                  intensity INTEGER)''')
    conn.commit()
    conn.close()

def log_attack(attack_type, target_ip, target_port, duration, intensity):
    conn = sqlite3.connect('config/attack_logs.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO logs (timestamp, attack_type, target_ip, target_port, duration, intensity) VALUES (?, ?, ?, ?, ?, ?)",
              (timestamp, attack_type, target_ip, target_port, duration, intensity))
    conn.commit()
    conn.close()