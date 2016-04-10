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

    def getPatiantDetails(patientid=none, patientsurname=none, patientaddress=none):
        """Returns a patient object depending on search parameters """
        if patientid != none:
            p = patient(self.db['patients'].find_one({'id': patientid}))    #There is only going to be one patient with that ID.
        else:
            #TODO Impliment get patient by name
            return none
        return p

    def getPatiantLocations(locationid=none, locationname=none, locationaddress=none):
        """ Returns the locations of a patient """
        if patientid != none:
            p = patient(self.db['locations'].find_one({'id': locationid}))    #There is only going to be one patient with that ID.
        #Possibly not required ever
        return p

    def write(patient):
        """Writes a patient object to the database - Make sure to exclude the locations from the data written"""
        if self.db['patients'].insert_one(patient.patientData) != 0:
            return True
        else:
            return False
        return 


