""" Patiant object  - Basically just contains the methods you might want to perform on the patiant data. So not much really! """

class patient:

    patientData = dict()

    def __init__(self,jsonPatient):
        """ constructor, takes the dictionary of patient data """
        return

    def setLocations(self,locations):
        """ Adds a locations field to the patient data. Must be coupled manually because we want to keep them seperate really """
        self.patientData
        return 

    def getField(self,field):
        """ Returns the field from patientData. We have a specific method for this so we can catch fields that don't exist."""
        return patientData[field]

