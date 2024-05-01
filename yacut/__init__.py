from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from settings import Config


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import api_views
    app.register_blueprint(api_views.bp)
    # todo
    # app.add_url_rule('/', endpoint='')

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index_view')

    # todo
    # from . import error_handlers
    # app.register_blueprint(error_handlers.bp)

    return app
