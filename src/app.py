import mysql.connector
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Get', methods=['GET'])
def Get():
  mydb = connect()
  datalist = []
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM user_details")
  myresult = mycursor.fetchall()
  for x in myresult:
      datalist.append(x)
  return str(datalist)

@app.route('/Post', methods=['POST'])
def Post():
  values = request.json
  mydb = connect()
  mycursor = mydb.cursor()
  sql = "INSERT INTO user_details (username, password, firstname, lastname, age) VALUES (%s, %s, %s, %s, %s)"
  values = (values[0], values[1], values[2], values[3], values[4])
  mycursor.execute(sql, values)
  mydb.commit()
  return 'Table has been updated.'


def connect():
  mydb = mysql.connector.connect(
    host="localhost",
    user="dennisceker",
    password="0987654321",
    database="users"
  )
  return mydb
