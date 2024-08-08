from flask import Flask
from flask_socketio import SocketIO
from models import db
from socketio_manager import socketio
from message import message_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(message_blueprint)

    socketio.init_app(app)

    return app

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)
