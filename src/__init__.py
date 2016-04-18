from flask import Flask

import settings

import check
from analyze import analyzeID, analyzeName
from database import databaseConnection
import json


app = Flask(__name__)

@app.route('/')
def home():
    return "Home page."

@app.route('/checkid/<pid>', methods=['GET'])
def checkid(pid=None):    #Takes an ID, finds it in the DB, and checks if it has anthrax

    database = databaseConnection(settings.dbString,settings.dbPort, "quinteq") #Connect to db
    ret = dict()
    ret['percentage_chance'] = round(check.checkID(database,pid)) #check the ID

    return json.dumps(ret)

@app.route('/checkname/<surname>', methods=['GET'])
def checkName(name=None):    #Takes a surname, finds it in the DB, and analyzes the person's path from that point. Should return any other people who might have anthrax in the area
    database = databaseConnection(settings.dbString,settings.dbPort, "quinteq") #Connect to db
    return check.checkName(database,name)

@app.route('/analyzeid/<pid>', methods=['POST'])
def analyzeid(pid=None):    #Takes an ID, finds it in the DB, and checks if it has anthrax. Should return any other people who might have anthrax in the area
    database = databaseConnection(settings.dbString,settings.dbPort, "quinteq") #Connect to db
    return False

@app.route('/analyzename/<surname>', methods=['POST'])
def analyzeName(name=None):    #Takes a surname, finds it in the DB, and checks if it has anthrax
    database = databaseConnection(settings.dbString,settings.dbPort, "quinteq") #Connect to db

    return False

@app.route('/alertStatus/')
def alertStatus():  #Returns alert status
    return False

if __name__ == '__main__':
    app.run(debug=True)
