""" Has methods for doing database stuff in """
from pymongo import MongoClient

class databaseConnection:

    client = none
    db = none

    def __init__(self, connectString, port, database):
        """ Initialises database connection. Returns database object""" 

        #TODO Error check here for connection
        self.client = MongoClient(connecString, port)
        
        self.db = self.client[database] # get our DB

        return self 

    def connect(self, connectionString, port):
        """auxilary method for changing the connection for the DB """
        return self.__init__(connectString,port)

    def getPatiantDetails(patiantid=none, patiantsurname=none, patiantaddress=none):
        """Returns a patiant object depending on search parameters """
        if patiantid != none:
            p = patient(self.db['patiants'].find_one({'id': patiantid}))    #There is only going to be one patiant with that ID.
        else:
            #TODO Impliment get patiant by name
            return none
        return p

    def getPatiantLocations(locationid=none, locationname=none, locationaddress=none):
        """ Returns the locations of a patiant """
        if patiantid != none:
            p = patient(self.db['locations'].find_one({'id': locationid}))    #There is only going to be one patiant with that ID.
        #Possibly not required ever
        return p

    def write(patiant):
        """Writes a patiant object to the database - Make sure to exclude the locations from the data written"""
        if self.db['patiants'].insert_one(patiant.patiantData) != 0:
            return True
        else:
            return False
        return 


