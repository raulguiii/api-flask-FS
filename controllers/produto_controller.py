# controllers/produto_controller.py
from flask import Blueprint, request, jsonify
from models.produto import Produto

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produto', methods=['POST'])
def create_produto():
    data = request.json
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    preco = data.get('preco')

    if not nome or quantidade is None or preco is None:
        return jsonify({"error": "Nome, quantidade, and preco are required"}), 400

    if not isinstance(quantidade, int) or quantidade < 0:
        return jsonify({"error": "Quantidade must be a non-negative integer"}), 400

    if not isinstance(preco, (int, float)) or preco < 0:
        return jsonify({"error": "Preco must be a non-negative number"}), 400

    try:
        Produto.create_produto(nome, quantidade, preco)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Produto created successfully"}), 201

@produto_bp.route('/produto/<int:produto_id>', methods=['PUT'])
def update_produto(produto_id):
    data = request.json
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    preco = data.get('preco')

    if nome is None and quantidade is None and preco is None:
        return jsonify({"error": "At least one field (nome, quantidade, preco) must be provided"}), 400

    if quantidade is not None and (not isinstance(quantidade, int) or quantidade < 0):
        return jsonify({"error": "Quantidade must be a non-negative integer"}), 400

    if preco is not None and (not isinstance(preco, (int, float)) or preco < 0):
        return jsonify({"error": "Preco must be a non-negative number"}), 400

    produto = Produto.get_produto(produto_id)
    if produto is None:
        return jsonify({"error": "Produto not found"}), 404

    Produto.update_produto(produto_id, nome, quantidade, preco)

    return jsonify({"message": "Produto updated successfully"})

@produto_bp.route('/produto', methods=['GET'])
def list_produtos():
    produtos = Produto.list_produtos()
    return jsonify([dict(produto) for produto in produtos])

@produto_bp.route('/produto/<int:produto_id>', methods=['GET'])
def get_produto(produto_id):
    produto = Produto.get_produto(produto_id)
    if produto is None:
        return jsonify({"error": "Produto not found"}), 404
    return jsonify(dict(produto))
