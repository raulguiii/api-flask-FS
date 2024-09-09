# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    is_active = data.get('is_active', True)  # Assume `True` se não fornecido
    cpf_cnpj = data.get('cpf_cnpj')

    if not name or not email or not password or not cpf_cnpj:
        return jsonify({"error": "Name, email, password, and cpf_cnpj are required"}), 400

    if not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' must be a boolean"}), 400

    try:
        with get_db() as db:
            db.execute(
                'INSERT INTO usuarios (name, email, password, is_active, cpf_cnpj) VALUES (?, ?, ?, ?, ?)',
                (name, email, password, is_active, cpf_cnpj)
            )
            db.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "User with this email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User created successfully"}), 201


@app.route('/usuario/<int:user_id>', methods=['PUT'])
def update_usuario(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    cpf_cnpj = data.get('cpf_cnpj')
    is_active = data.get('is_active')

    if not name or not email or not password or not cpf_cnpj:
        return jsonify({"error": "Name, email, password, and cpf_cnpj are required"}), 400

    if is_active is not None and not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' must be a boolean"}), 400

    with get_db() as db:
        cursor = db.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        user = cursor.fetchone()

        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.execute(
            'UPDATE usuarios SET name = ?, email = ?, password = ?, cpf_cnpj = ?, is_active = ? WHERE id = ?',
            (name, email, password, cpf_cnpj, is_active, user_id)
        )
        db.commit()

    return jsonify({"message": "User updated successfully"})

@app.route('/usuario/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    with get_db() as db:
        cursor = db.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        user = cursor.fetchone()

        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(dict(user))

@app.route('/usuario/<int:user_id>/status', methods=['PUT'])
def update_usuario_status(user_id):
    data = request.json
    is_active = data.get('is_active')

    if is_active is None or not isinstance(is_active, bool):
        return jsonify({"error": "Field 'is_active' is required and must be a boolean"}), 400

    with get_db() as db:
        cursor = db.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        user = cursor.fetchone()

        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.execute(
            'UPDATE usuarios SET is_active = ? WHERE id = ?',
            (is_active, user_id)
        )
        db.commit()

    return jsonify({"message": "User status updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)
