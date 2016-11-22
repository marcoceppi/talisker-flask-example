from logging import getLogger

from flask import Flask


app = Flask(__name__)
logger = getLogger(__name__)


@app.route('/')
def hello_world():
    logger.info('root handler', extra={'lang': 'en'})
    return 'Hello, World!'


def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
