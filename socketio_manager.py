from flask_socketio import SocketIO, emit
from models import db, Message
import random

socketio = SocketIO()

# Sample automated responses
AUTOMATED_RESPONSES = [
    "How can I assist you today?",
    "Thank you for your message!",
    "We're here to help. What do you need?",
    "Please let us know if you have any questions."
]

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    # Save the user message to the database
    new_message = Message(content=message)
    db.session.add(new_message)
    db.session.commit()

    # Broadcast the user message to all clients
    emit('message', message, broadcast=True)

    # Send an automated response
    automated_response = random.choice(AUTOMATED_RESPONSES)
    new_response = Message(content=automated_response)
    db.session.add(new_response)
    db.session.commit()

    # Broadcast the automated response to all clients
    emit('message', automated_response, broadcast=True)
