import os
from app import create_app
from config import DevelopmentConfig, ProductionConfig

if __name__ == '__main__':
    flask_env = os.getenv('FLASK_ENV', 'development')
    config = ProductionConfig if flask_env == 'production' else DevelopmentConfig

    app = create_app(config)
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)
