from flask import Flask
from flask_cors import CORS
from controllers.AccessibilityEventsController import ae_bp
from controllers.AdditionalDataController import ad_bp
from controllers.BatteryUsageController import bu_bp
from controllers.ConnectivityController import nc_bp
from controllers.DeviceStateController import ds_bp
from controllers.LocationDataController import ld_bp
from controllers.SensorController import sd_bp
from controllers.UsageStatsController import us_bp


def create_app():
    application = Flask(__name__)
    application.register_blueprint(ae_bp)
    application.register_blueprint(ad_bp)
    application.register_blueprint(bu_bp)
    application.register_blueprint(nc_bp)
    application.register_blueprint(ds_bp)
    application.register_blueprint(ld_bp)
    application.register_blueprint(sd_bp)
    application.register_blueprint(us_bp)
    CORS(application)
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
