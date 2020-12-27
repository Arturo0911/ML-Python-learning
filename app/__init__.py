from flask import Flask


def run_app():

    app = Flask(__name__)

    @app.route('/')

    def test():
        return "ok"

    return app