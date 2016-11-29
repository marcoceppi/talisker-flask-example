from os import getenv

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def setup_db(app, db=db):
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS', True)
    app.config['SQLALCHEMY_ECHO'] = getenv('SQLALCHEMY_ECHO', True)

    db.init_app(app)
    with app.app_context():
        db.create_all()
