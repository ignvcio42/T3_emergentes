from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET'])
def get_admins():
    return "Admin Route"
