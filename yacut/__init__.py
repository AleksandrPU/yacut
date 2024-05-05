from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import api_views
    app.register_blueprint(api_views.bp)

    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index_view')

    return app
