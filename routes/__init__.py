from flask import Blueprint

admin_bp = Blueprint('admin', __name__)
company_bp = Blueprint('company', __name__)
location_bp = Blueprint('location', __name__)
sensor_bp = Blueprint('sensor', __name__)
sensor_data_bp = Blueprint('sensor_data', __name__)
