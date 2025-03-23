from flask import Flask, render_template, request, redirect, url_for, Response
from app.utils import start_attack
import json
from app import app, limiter
import sqlite3
import time

@app.route('/')
def index():
    return render_template('index.html')

# Apply rate limiting to the attack route
@app.route('/attack', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def attack():
    if request.method == 'POST':
        attack_type = request.form['attack_type']
        target_ips = request.form['target_ips'].split(',')
        target_port = int(request.form['target_port'])
        duration = int(request.form['duration'])
        intensity = int(request.form['intensity'])
        packet_size = int(request.form.get('packet_size', 1024))
        headers = request.form.get('headers')
        spoof_ip = request.form.get('spoof_ip')

        start_attack(attack_type, target_ips, target_port, duration, intensity, packet_size, headers, spoof_ip)
        return redirect(url_for('logs'))
    return render_template('attack.html')


@app.route('/logs')
def logs():
    conn = sqlite3.connect('config/attack_logs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    logs = c.fetchall()
    conn.close()
    return render_template('logs.html', logs=logs)

@app.route('/stream')
def stream():
    last_id = request.args.get('last_id', 0, type=int)
    
    def generate(last_id):
        conn = sqlite3.connect('config/attack_logs.db')
        c = conn.cursor()
        while True:
            c.execute("SELECT * FROM logs WHERE id > ?", (last_id,))
            logs = c.fetchall()
            if logs:
                logs_json = []
                for log in logs:
                    logs_json.append({
                        "id": log[0],
                        "timestamp": log[1],
                        "attack_type": log[2],
                        "target_ip": log[3],
                        "target_port": log[4],
                        "duration": log[5],
                        "intensity": log[6]
                    })
                    last_id = log[0]
                yield f"data: {json.dumps(logs_json)}\n\n"
            time.sleep(1)
    
    return Response(generate(last_id), mimetype='text/event-stream')

