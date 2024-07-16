from flask import Blueprint

company_bp = Blueprint('company', __name__)

@company_bp.route('/company', methods=['GET'])
def get_companies():
    return "Company Route"
