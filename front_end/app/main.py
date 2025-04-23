from flask import Flask, render_template, request, redirect, flash
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
app.secret_key = 'secret123'

socketio = SocketIO(app)

headers = {
    'Content-Type': 'application/json'
}

API_URL = 'http://localhost:3000'  # Node.js API URL


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash('Email and password are required!', 'danger')
        socketio.emit('login_status', {'status': 'error'})
        return redirect('/')

    try:
        payload = {
            'email': email,
            'password': password
        }

        socketio.emit('login_status', {'status': 'loading'})
        response = requests.post(f'{API_URL}/airbnb/login', json=payload, headers=headers)

        if response.status_code == 200 and response.json().get('response') == 'True':
            flash('Login successful!', 'success')
            socketio.emit('login_status', {'status': 'success'})
            return redirect('/main')
        else:
            flash('Login failed. Try again.', 'danger')
            socketio.emit('login_status', {'status': 'error'})
    except Exception as e:
        flash(f'API Error: {str(e)}', 'danger')
        socketio.emit('login_status', {'status': 'error'})

    return redirect('/')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
