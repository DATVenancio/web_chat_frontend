from flask import Flask, render_template,request
from flask_socketio import SocketIO,send

app = Flask(__name__)


#routes
@app.route("/")
@app.route("/chat", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/chat", methods=["POST"])
def index():
    username = request.form.get("username")
    return render_template("index.html",username=username)



if __name__ == "__main__":
    app.run(port=5010)
    