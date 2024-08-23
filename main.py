from flask import Flask, render_template, request, session,redirect
from flask_socketio import join_room,leave_room, send, SocketIO
import random #generates random room numbers
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
socketio = SocketIO(app)

#:Homepage: Route to create or Check a chatroom
@app.route("/", methods = ["POST", "GET"])
def home():
    return render_template("home.html")  #calls html code to screen

#Room page: Join chatroom

if __name__ == "__main__":
    socketio.run(app,debug=True)