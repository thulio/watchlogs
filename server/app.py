from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/_health')
def health():
    return 'OK'


if __name__ == '__main__':  # pragma: no cover
    import os

    app.run(debug=os.getenv('DEBUG', '0') == '1')
