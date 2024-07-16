from flask import Blueprint

sensor_data_bp = Blueprint('sensor_data', __name__)

@sensor_data_bp.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    return "Sensor Data Route"
