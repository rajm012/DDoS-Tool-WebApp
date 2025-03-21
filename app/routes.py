from flask import Flask, render_template, request, redirect, url_for, Response
from app.utils import start_attack
import json
from app import app
import sqlite3
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attack', methods=['GET', 'POST'])
def attack():
    if request.method == 'POST':
        attack_type = request.form['attack_type']
        target_ip = request.form['target_ip']
        target_port = int(request.form['target_port'])
        duration = int(request.form['duration'])
        intensity = int(request.form['intensity'])
        
        # Start attack
        start_attack(attack_type, target_ip, target_port, duration, intensity)
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
    def generate():
        conn = sqlite3.connect('config/attack_logs.db')
        c = conn.cursor()
        last_id = request.args.get('last_id', 0, type=int)
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
    return Response(generate(), mimetype='text/event-stream')