# controllers/usuario_controller.py
from flask import Blueprint, request, jsonify
from models.usuario import Usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def list_usuarios():
    usuarios = Usuario.list_usuarios()
    return jsonify([dict(usuario) for usuario in usuarios])

@usuario_bp.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.json
    required_fields = ['name', 'email', 'password', 'cpf_cnpj']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Name, email, password, and cpf_cnpj are required"}), 400

    name = data['name']
    email = data['email']
    password = data['password']
    cpf_cnpj = data['cpf_cnpj']
    is_active = data.get('is_active', True)

    if not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' must be a boolean"}), 400

    try:
        Usuario.create_usuario(name, email, password, is_active, cpf_cnpj)
    except sqlite3.IntegrityError:
        return jsonify({"error": "User with this email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User created successfully"}), 201

@usuario_bp.route('/usuario/<int:user_id>', methods=['PUT'])
def update_usuario(user_id):
    data = request.json
    required_fields = ['name', 'email', 'password', 'cpf_cnpj']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Name, email, password, and cpf_cnpj are required"}), 400

    name = data['name']
    email = data['email']
    password = data['password']
    cpf_cnpj = data['cpf_cnpj']
    is_active = data.get('is_active')

    if is_active is not None and not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' must be a boolean"}), 400

    user = Usuario.get_usuario(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    Usuario.update_usuario(user_id, name, email, password, cpf_cnpj, is_active)

    return jsonify({"message": "User updated successfully"})

@usuario_bp.route('/usuario/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    user = Usuario.get_usuario(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(dict(user))

@usuario_bp.route('/usuario/<int:user_id>/status', methods=['PUT'])
def update_usuario_status(user_id):
    data = request.json
    is_active = data.get('is_active')

    if is_active is None or not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' is required and must be a boolean"}), 400

    user = Usuario.get_usuario(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    Usuario.update_usuario_status(user_id, is_active)

    return jsonify({"message": "User status updated successfully"})

@usuario_bp.route('/usuario/<int:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    try:
        user = Usuario.get_usuario(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        Usuario.delete_usuario(user_id)
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
