from app.configs.database import db
import sqlalchemy
from dataclasses import dataclass

db: sqlalchemy = db


@dataclass
class Character(db.Model):
    name: str
    description: str
    bounty: str
    country: str

    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    bounty = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(25), nullable=False)
