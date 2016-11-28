from functools import wraps

from flask_sqlalchemy import SQLAlchemy

from helloworld.models import User


def get_connection(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
	'SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
	'SQLALCHEMY_TRACK_MODIFICATIONS', True)
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO', True)

    db = SQLAlchemy(app)
    db.create_all()
    return db


@wraps(fn)
def wrap_with_connection(fn, app):
    def wrapper(*args, **kwargs):
        kwargs['db'] = get_connection(app)
        return fn(*args, **kwargs)

    return wrapper
