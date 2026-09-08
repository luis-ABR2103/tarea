from flask import Blueprint
from Controllers.InstructorController import instructorController

ins_bp = Blueprint('ins_bp', __name__)

@ins_bp.route('/', methods=['GET'])
def home():
    instructorController.show()

@ins_bp.route('/', methods=['POST'])
def add():
    return "agregar instructor"