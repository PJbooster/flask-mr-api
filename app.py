from flask import Flask
from flask_restful import Resource, Api

from api.resources.lotto import Lotto


def create_app():
    app = Flask(__name__)

    ## Initialize Config

    api = Api(app)
    app.config.from_pyfile('config.py')
    api.add_resource(Lotto, '/lotto')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.debug = True
    app.run(host='0.0.0.0', port=port)
