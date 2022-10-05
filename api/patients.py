from flask import Blueprint, request, jsonify

patients_blueprint = Blueprint('patients', __name__)

@patients_blueprint.route('', methods=['POST'])
def add_patient():
    data = request.json
    # Handle the patient addition logic
    return jsonify({'message': 'Patient added', 'data': data}), 201

@patients_blueprint.route('', methods=['GET'])
def get_patients():
    # Handle patient retrieval logic
    return jsonify({'message': 'Patients retrieved successfully'}), 200
