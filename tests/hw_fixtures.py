from os import remove
from os.path import exists

from pytest import fixture

from helloworld import app
from helloworld.database import db, setup_db


@fixture(scope='session')
def client():
    app.config['TESTING'] = True
    return app.test_client()


@fixture(scope='function')
def database():
    app.config['TESTING'] = True
    db_file = 'sqlite:////tmp/hw_test.db'

    if exists(db_file):
        remove(db_file)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_file
    db = setup_db(app)

    yield db

    with app.app_context():
        db.session.remove()
        db.drop_all()
