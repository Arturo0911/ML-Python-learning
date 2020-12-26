from flask import Flask



app = Flask(__name__)

@app.route('/')
def API_init():
    return "Here go the api meteorology"


if __name__ == '__main__':
    app.run(port = 4000, debug = True)
