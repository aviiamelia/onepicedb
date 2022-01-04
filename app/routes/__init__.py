from flask import Flask
from .characters_blueprint import bp_character


def init_app(app: Flask):
    app.register_blueprint(bp_character)
