from logging import getLogger

from flask import Flask, request

from helloworld.db import wrap_with_connection
from helloworld.models import User


app = Flask(__name__)
logger = getLogger(__name__)


@app.route('/')
def hello_world():
    logger.info('root handler', extra={'lang': 'en'})
    return 'Hello, World!'


@app.route('/users/', methods=['POST'])
@wrap_with_connection(app)
def username(db):
    user = User(request.form['username'])
    db.session.add(user)
    db.session.commit()
    logger.info('username: {}'.format(request.form['username']))
    return request.form['username']


@app.route('/users/')
@wrap_with_connection(app)
def usernames(db):
    users = User.query.all()
    logger.info('users: {}'.format(users))
    return str(users)


def main():
    debug = os.getenv('DEBUG', 'true').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
