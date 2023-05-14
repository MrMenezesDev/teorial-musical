from flask import Flask
from functools import wraps
from flask import jsonify

from teoria_musical.acordes import acorde
from teoria_musical.escalas import ESCALAS, escala
from teoria_musical.campo_harmonico import campo_harmonico
from teoria_musical.notas import NOTAS


app = Flask(__name__)


def handle_error(f):
    """
    # Decoradro de Error
    Para tratar as exceções vindouras de NOTAS e ESCALAS
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError:
            return jsonify({'notas': list(NOTAS)}), 404
        except KeyError:
            return jsonify({'escalas': list(ESCALAS.keys())}), 404
        except Exception:
            return jsonify({'error': 'Internal Server Error'}), 500
    return wrapper


@app.route("/")
@handle_error
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/escala")
@handle_error
def get_escala(tonica: str, tonalidade: str):
    return jsonify({'error': escala(tonica, tonalidade).values()}, 200)


@app.route("/acorde")
@handle_error
def get_acorde(tonica: str, tonalidade: str):
    return jsonify({'error': acorde(tonica, tonalidade).values()}, 200)


@app.route("/campo_hamonico")
@handle_error
def get_campo_harmonico(tonica: str, tonalidade: str):
    return jsonify({'error': campo_harmonico(tonica, tonalidade).values()}, 200)
