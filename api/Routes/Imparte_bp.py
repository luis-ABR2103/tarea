from flask import Blueprint
from Controllers.ImparteController import imparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def home():
    imparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    return "agregar imparte"