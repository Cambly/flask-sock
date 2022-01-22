from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from flask import Flask, render_template
from flask_sock import Sock
app = Flask(__name__)

sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)


if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 5000), app).serve_forever()
