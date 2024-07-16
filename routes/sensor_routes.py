from flask import Blueprint

sensor_bp = Blueprint('sensor', __name__)

@sensor_bp.route('/sensor', methods=['GET'])
def get_sensors():
    return "Sensor Route"
