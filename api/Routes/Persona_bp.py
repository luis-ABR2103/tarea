from flask import Blueprint
from Controllers.PersonaController import personaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def home():
    personaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return "agregar persona"