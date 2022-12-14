import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = "postgres://lbyxwmuqvbndrv:948908345954624da81b9a539c830d5122aff868c7f927efc3ce5e5a2bf31350@ec2-44-205-63-142.compute-1.amazonaws.com:5432/df6ube44s5bk3",
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from . import controler
    app.register_blueprint(controler.bp)

    return app

if __name__ == '__main__':
        # Production
        app.run_server(debug=True)