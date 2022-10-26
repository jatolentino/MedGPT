from flask import Blueprint, request, jsonify

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('', methods=['POST'])
def create_chat():
    data = request.json
    # Handle the chat creation logic
    return jsonify({'message': 'chat created', 'data': data}), 201
