""" Has methods for doing database stuff in """
from pymongo import MongoClient
import patient

class databaseConnection:

    client = None
    db = None

    def __init__(self, connectString, port, database):
        """ Initialises database connection. Returns database object""" 

        #TODO Error check here for connection
        self.client = MongoClient(connectString, port)
        
        self.db = self.client[database] # get our DB

        return 

    def connect(self, connectionString, port):
        """auxilary method for changing the connection for the DB """
        return self.__init__(connectString,port)

    def getPatientDetails(self,patientid=None, patientsurname=None, patientaddress=None):
        """Returns a patient object depending on search parameters """
        if patientid != None:
            p = self.db['patients'].find({"id": int(patientid)})    #There is only going to be one patient with that ID.
        else:
            #TODO Impliment get patient by name
            return None
        return p

    def getPatientLocations(self,locationid=None, locationname=None, locationaddress=None):
        """ Returns the locations of a patient """
        if patientid != None:
            p = patient.patient(self.db['locations'].find_one({'id': locationid}))    #There is only going to be one patient with that ID.
        #Possibly not required ever
        return p

    def write(self,patient):
        """Writes a patient object to the database - Make sure to exclude the locations from the data written"""
        if self.db['patients'].insert_one(patient.patientData) != 0:    #We should be making sure we're not creating duplicates here
            return True
        else:
            return False
        return 


