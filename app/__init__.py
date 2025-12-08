from flask import Flask
import logging
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    logging.basicConfig(
        level=app.config['LOGGING_LEVEL'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    from app.routes.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        logging.error(f'Internal server error: {error}')
        return {'error': 'Internal server error'}, 500

    return app
