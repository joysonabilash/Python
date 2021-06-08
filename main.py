from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return 'Hello World'


@app.route("/view", methods=['GET'])
def favicon():
    return 'Hello View'


if __name__ == '__main__':
    app.run()