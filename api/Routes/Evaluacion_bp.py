from flask import Blueprint
from Controllers.EvaluacionController import evaluacionController

eva_bp = Blueprint('eva_bp', __name__)

@eva_bp.route('/', methods=['GET'])
def home():
    evaluacionController.show()

@eva_bp.route('/', methods=['POST'])
def add():
    return "agregar evaluacion"