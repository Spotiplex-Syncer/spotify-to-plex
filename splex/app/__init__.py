from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from services.confighandler import read_config  # Assuming you have a custom config handler
from celery import Celery

def create_celery_app(app=None):
    """
    Initialize Celery helper function.
    """
    app = app or create_app('config.py')
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
                
    celery.Task = ContextTask
    return celery

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    # Initialize plugins
    socketio = SocketIO(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Celery configuration
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    celery = create_celery_app(app)

    # Register Blueprints, if you have any
    # from .views import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # SocketIO events, example
    @socketio.on('connect')
    def test_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def test_disconnect():
        print('Client disconnected')

    # Flask-Login configuration
    @login_manager.user_loader
    def load_user(user_id):
        # Your user loading logic here
        return None

    return app, socketio, celery

# If you are using factory pattern, the celery worker needs to import the celery instance
app, socketio, celery = create_app('config.py')

if __name__ == '__main__':
    socketio.run(app, debug=True)
