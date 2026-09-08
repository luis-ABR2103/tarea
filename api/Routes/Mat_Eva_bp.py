from flask import Blueprint
from Controllers.Mat_EvaController import matEvaController

mate_bp = Blueprint('mate_bp', __name__)

@mate_bp.route('/', methods=['GET'])
def home():
    matEvaController.show()

@mate_bp.route('/', methods=['POST'])
def add():
    return "agregar mat_eva"