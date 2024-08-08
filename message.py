# message.py

from flask_socketio import join_room, leave_room, emit
from socketio_manager import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', 'Welcome to the chat!')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('message', f"{data['username']} has entered the room.", room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    emit('message', f"{data['username']} has left the room.", room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    emit('message', data['message'], room=room)

@socketio.on('get_history')
def handle_get_history(data):
    room = data['room']
    # Here you can fetch and return the chat history for the room
    history = []  # Replace with actual history retrieval logic
    emit('history', history)
