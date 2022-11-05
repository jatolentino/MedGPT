from flask import Blueprint, jsonify

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('', methods=['GET'])
def get_data():
    # Handle data retrieval logic
    return jsonify({'message': 'Data retrieved successfully'}), 200
