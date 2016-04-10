from flask import Flask

import settings

from check import checkID, checkName
from analyze import analyzeID, analyzeName


app = Flask(__name__)

@app.route('/')
def home():
    return "Home page."

@app.route('/checkid/<id>', methods=['GET'])
def checkID(id):    #Takes an ID, finds it in the DB, and checks if it has anthrax
    database = databaseConnection(settings.dbString,setting.dbPort) #Connect to db
    return checkID(database,id) #check the ID

@app.route('/checkname/<surname>', methods=['GET'])
def checkName(name):    #Takes a surname, finds it in the DB, and analyzes the person's path from that point. Should return any other people who might have anthrax in the area
    database = databaseConnection(settings.dbString,setting.dbPort) #Connect to db
    return checkName(database,name)

@app.route('/analyzeid/<id>', methods=['POST'])
def analyzeID(id):    #Takes an ID, finds it in the DB, and checks if it has anthrax. Should return any other people who might have anthrax in the area
    return False

@app.route('/analyzename/<surname>', methods=['POST'])
def analyzeName(name):    #Takes a surname, finds it in the DB, and checks if it has anthrax
    return False

@app.route('/alertStatus/')
def alertStatus():  #Returns alert status
    return False

if __name__ == '__main__':
    app.run()
