from app.models.characterModel import Character
from flask import request, current_app, jsonify


def create_character():
    session = current_app.db.session
    data = request.get_json()
    character = Character(**data)
    session.add(character)
    session.commit()
    return {
        "id": character.id,
        "name": character.name,
        "description": character.description,
        "bounty": character.bounty,
        "country": character.country,
    }, 201


def get_characters():
    characters = Character.query.all()
    return jsonify(characters), 200
