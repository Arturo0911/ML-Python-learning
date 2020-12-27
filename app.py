from flask import Flask
# from app import run_app


app = Flask(__name__)

@app.route('/')
def API_init():
    return "Here go the api meteorology"


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
