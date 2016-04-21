""" Script which does all the analysis for checking area of people. """

from bson.son import SON
from patient import patient

def analyzeID(db, Id):  
    """Takes an ID, tracks the movement attached to it and finds other people that may have come in contact""" 
    p = patient(db.getPatientDetails(patientid=Id))
    analyze(p)

    return none

def analyzeName(db, name):  
    """ Takes an ID, tracks the movement attached to it and finds other people that may have come in contact""" 
    p = patient(db.getPatientDetails(patientsurname=name))
    return none

def analyze(p):
    """ Takes a Patiant and returns the percentage chance that they have anthrax"""

    
    for locations in p.patientData['locations']: #For ever location pair
        #Grab all the docs with intersecting locations
        intersectingDocs.append( db.db.tracking.find({"locations":{"$near":{"$geometry":{"type":"Point", "coordinates": [locations[0],locations[1]]}}}}))

    ret = list()
    for d in intersectingDocs:
        ret.append(d['id'])

    return ret

    

