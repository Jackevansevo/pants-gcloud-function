import flask
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


def handler(request: flask.Request) -> flask.Response:
    return {
        "flask": flask.__version__,
        "FlaskSQLAlchemy": flask_sqlalchemy.__version__,
        "sqlalchemy": sqlalchemy.__version__,
    }


def create_app():
    app = flask.Flask(__name__)

    @app.get("/")
    def index():
        return handler(flask.request)

    return app
