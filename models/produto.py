# models/produto.py
import sqlite3
from config.config import Config

def get_db():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Produto:
    @staticmethod
    def list_produtos():
        with get_db() as db:
            cursor = db.execute('SELECT * FROM produtos')
            return cursor.fetchall()

    @staticmethod
    def create_produto(nome, quantidade, preco):
        with get_db() as db:
            db.execute(
                'INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)',
                (nome, quantidade, preco)
            )
            db.commit()

    @staticmethod
    def get_produto(produto_id):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,))
            return cursor.fetchone()

    @staticmethod
    def update_produto(produto_id, nome=None, quantidade=None, preco=None):
        with get_db() as db:
            if nome is not None:
                db.execute('UPDATE produtos SET nome = ? WHERE id = ?', (nome, produto_id))
            if quantidade is not None:
                db.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (quantidade, produto_id))
            if preco is not None:
                db.execute('UPDATE produtos SET preco = ? WHERE id = ?', (preco, produto_id))
            db.commit()
