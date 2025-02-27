from flask import Blueprint, request, jsonify
from repositories import ObjectiveRepository
from models import ObjectiveJSONEncoder
import json

bp = Blueprint('objectifs', __name__)

objectives = [
    { "name": "Apprendre le Python", "position": 1, "description": "Apprendre les bases du langage Python", "tags": ["Python", "Apprentissage"], "tier": 1 }
]

# Add CORS headers
@bp.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response

@bp.route('/objectives', methods=['GET'])
def get_objectives():
    repository = ObjectiveRepository()
    return json.dumps(repository.get_all(), cls=ObjectiveJSONEncoder), 200

@bp.route('/objectives', methods=['POST'])
def create_objective():
    data = request.json
    objectives.append(data)
    return jsonify(data), 201

@bp.route('/objectives/<int:index>', methods=['PUT'])
def update_objective(index):
    if index < 0 or index >= len(objectives):
        return jsonify({'error': 'Objectif non trouvé'}), 404
    data = request.json
    objectives[index] = data
    return jsonify(data), 200

def init_routes(app):
    app.register_blueprint(bp)