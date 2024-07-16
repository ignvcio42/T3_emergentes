from flask import Blueprint

location_bp = Blueprint('location', __name__)

@location_bp.route('/location', methods=['GET'])
def get_locations():
    return "Location Route"
