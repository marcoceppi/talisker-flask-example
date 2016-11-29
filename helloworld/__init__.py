from logging import getLogger

from flask import Flask, request
import talisker

from helloworld.database import db, setup_db
from helloworld.models import User


app = Flask(__name__)
setup_db(app)
logger = getLogger(__name__)

# Provide correct X-VCS-Revision value
with open('version-info.txt') as f:
    talisker.revision.set(f.read())


@app.route('/')
def hello_world():
    logger.info('root handler', extra={'lang': 'en'})
    return 'Hello, World!'


@app.route('/users/', methods=['POST'])
def username():
    user = User(request.form['username'])
    db.session.add(user)
    db.session.commit()
    logger.info('username: {}'.format(request.form['username']))
    return request.form['username']


@app.route('/users/')
def usernames():
    users = User.query.all()
    logger.info('users: {}'.format(users))
    return str(users)


def main():
    debug = os.getenv('DEBUG', 'true').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
