from flask import Flask, render_template, request, session,redirect, url_for
from flask_socketio import join_room,leave_room, send, SocketIO
import random #generates random room numbers
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
socketio = SocketIO(app)

rooms = {}

def generate_unique_code(Length):
    while True:
        code = ""
        for _ in range (Length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break
    return code

#:Homepage: Route to create or Check a chatroom
@app.route("/", methods = ["POST", "GET"])
def home():
    session.clear
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
             return render_template("home.html", error ="please enter your name.", code=code, name=name)
        
        if join != False and not code:
            return render_template("home.html", error ="please room code.",code=code, name=name )
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members":0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error ="Room does not exist", code=code, name=name)
        
        #Temporary way to store user data
        session["room"] = room
        session["name"] = name
        #Pushes user to the room route
        return redirect(url_for("room"))

    return render_template("home.html")  #calls html code to screen

@app.route("/room")
def room():
    return render_template("room.html")

#Room page: Join chatroom

if __name__ == "__main__":
    socketio.run(app,debug=True)