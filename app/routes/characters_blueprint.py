from flask import Blueprint
from app.controllers.characters_controller import create_character
from app.controllers.characters_controller import get_characters

bp_character = Blueprint("bp_character", __name__, url_prefix="/characters")
bp_character.post("")(create_character)
bp_character.get("")(get_characters)
