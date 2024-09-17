# app.py
from flask import Flask
from controllers.usuario_controller import usuario_bp
from controllers.produto_controller import produto_bp

app = Flask(__name__)

app.register_blueprint(usuario_bp)
app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True)
