from flask import Flask
from database import db
from routes.admin_routes import admin_bp
from routes.company_routes import company_bp
from routes.location_routes import location_bp
from routes.sensor_routes import sensor_bp
from routes.sensor_data_routes import sensor_data_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(admin_bp, url_prefix='/api/v1')
app.register_blueprint(company_bp, url_prefix='/api/v1')
app.register_blueprint(location_bp, url_prefix='/api/v1')
app.register_blueprint(sensor_bp, url_prefix='/api/v1')
app.register_blueprint(sensor_data_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
