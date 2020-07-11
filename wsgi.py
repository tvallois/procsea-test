import os
from flask_migrate import Migrate
from procsea_test.application import create_app
from procsea_test import db

app_env = os.environ.get("FLASK_ENV", "development")
os.environ["LOG_LEVEL"] = os.environ.get("LOG_LEVEL") or "WARNING"

app = create_app(app_env)
migrate = Migrate(app, db)
