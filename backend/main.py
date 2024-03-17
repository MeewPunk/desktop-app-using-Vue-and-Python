 # coding=utf8
# env\Scripts\activate

from flask_socketio import SocketIO
from flask import Flask, render_template
from flask_cors import CORS
import sys,os
import threading
import webview

port = 8080

template_folder = os.path.abspath('templates')
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY"
app = Flask(__name__, static_url_path=r'/static')
app = Flask(__name__, template_folder=template_folder)
CORS(app)
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def index(): 
    return render_template("index.html",)

@app.route('/v1/login',  methods=['POST'])
def login():

    print('login')
    return {"status": "success", "message": "Login success", "data": {}}

def start_server():
    socketio.run(app, port=port)

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window(f"Desktop App Using Vue", f"http://127.0.0.1:{port}", width=1600, height=900)
    webview.start()

