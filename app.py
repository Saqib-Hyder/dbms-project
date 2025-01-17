from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

cnx = mysql.connector.connect(
    user="root", password="1234", host="localhost", database="dbms"
)
cursor = cnx.cursor()
app = Flask(__name__)


@app.route("/rooms", methods=["POST"])
def save_rooms():
    room_id = request.form.get("room_id")
    cost_room = request.form.get("cost_room")
    query = "INSERT INTO rooms VALUES({}, {})".format(room_id, cost_room)
    cursor.execute(query)
    cnx.commit()
    return redirect(url_for("get_rooms"))


@app.route("/rooms/insert")
def get_rooms():
    return render_template("index.html")


@app.route("/rooms/display")
def dis_rooms():
    rooms = []
    query = "SELECT room_no,room_cost FROM rooms "
    cursor.execute(query)
    for (room_no, room_cost) in cursor:
        room = {"num": room_no, "cost": room_cost}
        rooms.append(room)
        print(rooms)
    return render_template("dis_room.html", disprooms=rooms)


@app.route("/book/<num>", methods=["GET", "POST"])
def book(num):
    # logic to insert booking details to booking table
    # query = "insert into book values({})".format(num)
    # cursor.execute(query)
    # cnx.commit()
    return render_template("add_name.html", id=num)


@app.route("/add_name", methods=["POST"])
def booking():
    # logic to insert booking details to booking table
    cust_id = request.form.get('cust_id')
    cust_name = request.form.get('cust_name')
    book_date = request.form.get('add_date')
    query = "INSERT INTO book VALUES({},'{}','{}')".format(
        cust_id, cust_name, book_date)
    cursor.execute(query)
    cnx.commit()
    return render_template("success.html")


@app.route("/sort")
def sorr_rooms():
    rooms = []
    query = "SELECT room_no,room_cost FROM rooms ORDER BY room_cost;"
    cursor.execute(query)
    for (room_no, room_cost) in cursor:
        room = {"num": room_no, "cost": room_cost}
        rooms.append(room)
    return render_template("dis_room.html", disprooms=rooms)


@app.route('/')
def start_page():
    return render_template("welcome.html")


@app.route('/inpdate')
def inpdate():
    return render_template("input-date.html")


@app.route('/getdate', methods=["POST"])
def get_date():
    particulardate = request.form.get('chosendate')
    query = "SELECT *  FROM rooms WHERE room_no NOT IN (SELECT booked_room FROM book WHERE booked_date='{}');".format(
        particulardate)
    cursor.execute(query)
    dis = []
    for (booked_room, cust_name) in cursor:
        room = {"num": booked_room, "cost": cust_name}
        dis.append(room)
    return render_template("dis_room.html", disprooms=dis)


@app.route("/takefood")
def dis_food():
    return render_template("ins_food.html")


@app.route("/ins_food", methods=['POST'])
def ins_food():
    food_id = request.form.get('food_id')
    food_name = request.form.get('food_name')
    food_time = request.form.get('food_time')
    query = "INSERT INTO food VALUES ({},'{}','{}')".format(
        food_id, food_name, food_time)
    cursor.execute(query)
    cnx.commit()
    return render_template ("success.html")
