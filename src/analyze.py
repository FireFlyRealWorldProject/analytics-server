""" Script which does all the analysis for checking area of people. """

from bson.son import SON
import json
from patient import patient
from database import trackingDB
import settings

def analyzeID(db, Id):  
    """Takes an ID, tracks the movement attached to it and finds other people that may have come in contact""" 
    p = patient(db.getPatientDetails(patientid=Id))
    ret = analyze(p)

    return json.dumps(ret, sort_keys=True)

def analyzeName(db, name):  
    """ Takes an ID, tracks the movement attached to it and finds other people that may have come in contact""" 
    p = patient(db.getPatientDetails(patientsurname=name))
    return none

def analyze(p):
    """ Takes a Patiant and returns the percentage chance that they have anthrax"""

    tDB = trackingDB(settings.dbString, settings.dbPort, "quinteq")
   

    intersectingDocs = list()
    patientLocations = tDB.getTracking(p.patientData['id'])
    for locations in patientLocations:
        for coordPairs in locations['locations']['coordinates']: #For ever location pair
            #Grab all the docs with intersecting locations
            intersectingDocs.append(tDB.db.tracking.find({"locations":{"$near":{"$geometry":{"type":"Point", "coordinates": [int(coordPairs[1]),int(coordPairs[0])]}}}}))

        ret = list()
        print(intersectingDocs[0].count())
        for d in intersectingDocs:
            for i in d:
                ret.append(i['patient_id'])

    return ret

    

