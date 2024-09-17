# models/usuario.py
import sqlite3
from config.config import Config

def get_db():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Usuario:
    @staticmethod
    def list_usuarios():
        with get_db() as db:
            cursor = db.execute('SELECT * FROM usuarios')
            return cursor.fetchall()

    @staticmethod
    def create_usuario(name, email, password, is_active, cpf_cnpj):
        with get_db() as db:
            db.execute(
                'INSERT INTO usuarios (name, email, password, is_active, cpf_cnpj) VALUES (?, ?, ?, ?, ?)',
                (name, email, password, is_active, cpf_cnpj)
            )
            db.commit()

    @staticmethod
    def get_usuario(user_id):
        with get_db() as db:
            cursor = db.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
            return cursor.fetchone()

    @staticmethod
    def update_usuario(user_id, name, email, password, cpf_cnpj, is_active):
        with get_db() as db:
            db.execute(
                'UPDATE usuarios SET name = ?, email = ?, password = ?, cpf_cnpj = ?, is_active = ? WHERE id = ?',
                (name, email, password, cpf_cnpj, is_active, user_id)
            )
            db.commit()

    @staticmethod
    def update_usuario_status(user_id, is_active):
        with get_db() as db:
            db.execute(
                'UPDATE usuarios SET is_active = ? WHERE id = ?',
                (is_active, user_id)
            )
            db.commit()

    @staticmethod
    def delete_usuario(user_id):
        with get_db() as db:
            db.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
            db.commit()
