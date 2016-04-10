""" Patiant object  - Basically just contains the methods you might want to perform on the patiant data. So not much really! """

class patient:

    patientData = dict()

    def __init__(self,jsonPatient):
        """ constructor, takes the dictionary of patient data """
        self.patientData = jsonPatient

        return

    def setLocations(self,db,locations):
        """ Adds a locations field to the patient data. Must be coupled manually because we want to keep them seperate really """
        self.patientData['locations'] = db.getPatientLocations(id=self.patientData['id'])
        return 

    def getField(self,field):
        """ Returns the field from patientData. We have a specific method for this so we can catch fields that don't exist."""
        try:
            data = patientData[field]
        except KeyError:
            return none

        return data

