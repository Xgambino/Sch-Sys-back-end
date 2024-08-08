import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, send

# Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    messages = db.relationship('Message', backref='author', lazy='dynamic')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Routes and socket events
@app.route('/')
def index():
    return 'Hello, Flask with SocketIO!'

@socketio.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    # In a real app, you would likely save the message to the database here
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
