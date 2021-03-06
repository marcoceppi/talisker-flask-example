from logging import getLogger
from os import path

from flask import Flask, jsonify, request
import talisker

from helloworld.database import db, setup_db
from helloworld.models import User


app = Flask(__name__)
setup_db(app)
logger = getLogger(__name__)

version_info_path = path.join(path.dirname(path.dirname(__file__)),
                              'version-info.txt')

if path.exists(version_info_path): # pragma: no cover
    # Provide correct X-VCS-Revision value
    with open(version_info_path) as f:
        talisker.revision.set(f.read())


@app.route('/')
def hello_world():
    logger.info('root handler', extra={'lang': 'en'})
    return 'Hello, World!'


@app.route('/users/', methods=['POST'])
def add_user():
    user = User(request.form['username'])
    db.session.add(user)
    db.session.commit()
    logger.info('username: {}'.format(request.form['username']))
    return jsonify(user.jsonify())


@app.route('/users/')
def list_users():
    users = User.query.all()
    logger.info('users: {}'.format(users))
    return jsonify(json_list=[u.jsonify() for u in users])


def main():
    debug = os.getenv('DEBUG', 'true').lower() == 'true' # pragma: no cover
    app.run(debug=debug, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
