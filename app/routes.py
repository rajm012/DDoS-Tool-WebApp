from flask import Flask, render_template, request, redirect, url_for, Response, flash
from app.utils import start_attack
import json
from app import app, limiter
import sqlite3
import time
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.database import add_user, get_user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if get_user(username):
            flash('Username already exists!', 'error')

        else:
            if add_user(username, password):
                flash('Account created successfully! Please log in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('An error occurred. Please try again.', 'error')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = get_user(username)

        if user_data and user_data['password'] == password:
            user = User(user_data['id'], user_data['username'])
            login_user(user)  # Log the user in
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        flash('Invalid credentials', 'error')
    return render_template('login.html')


# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))


# Protect routes
@app.route('/attack', methods=['GET', 'POST'])
@login_required
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

        # Start attack
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

