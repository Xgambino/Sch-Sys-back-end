from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from socketio_manager import socketio, init_socketio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)
migrate = Migrate(app, db)

init_socketio(app)

# Import message after initializing Flask extensions
from message import handle_connect, handle_disconnect, handle_join, handle_leave, handle_message, handle_get_history

if __name__ == '__main__':
    socketio.run(app, debug=True)
