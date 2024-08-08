from flask import Blueprint, request, jsonify
from models import db, Message

message_blueprint = Blueprint('message', __name__)

@message_blueprint.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages])

@message_blueprint.route('/messages', methods=['POST'])
def post_message():
    data = request.json
    new_message = Message(content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201
