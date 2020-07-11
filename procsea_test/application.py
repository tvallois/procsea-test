import os
from flask import Flask
from werkzeug.utils import import_string
from procsea_test.config import DevelopmentConfig, StagingConfig, TestConfig, ProductionConfig, Config
from procsea_test import db, io

def create_app(environment: str) -> Flask:
    (
        """
    Creates and initializes a new web application
    :param environment: Environment name.
    """
    )
    config_map = {
        "development": DevelopmentConfig(),
        "staging": StagingConfig(),
        "test": TestConfig(),
        "production": ProductionConfig(),
    }

    config_obj = config_map[environment.lower()]

    app = create_flask_app(environment, config_obj)

    return app


def create_flask_app(environment: str, config_obj: Config) -> Flask:
    (
        """
    Creates a Flask application
    :param environment: Environment name.
    :param config: Configuration to use.
    :return: A Flask app.
    """
    )
    app = Flask(__name__)

    with app.app_context():
        app.env = environment
        app.config.from_object(config_obj)
        db.init_app(app)
        io.init_app(app)
        register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    """
    Pass through all view.py files and register
    any app field found as a blueprint
    :param app: The Flask app.
    """
    root_folder = "oauth_server"

    for dir_name, _, _ in os.walk(root_folder):
        module_name = ("{}{}").format(dir_name.replace(os.path.sep, "."), ".views")
        module_path = os.path.join(dir_name, "views.py")

        if os.path.exists(module_path):
            module = import_string(module_name)
            obj = getattr(module, "app", None)
            if obj:
                app.register_blueprint(obj)

