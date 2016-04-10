""" Checks symptoms of a patient to see if they have anthrax or not """


def check(patient):
    """Takes a patient object and checks it for symptoms"""
    return False

def checkID(db,patientID):
    """ Checks if the patient has anthrax, sets that status in the DB, and returns true or false """
    print("PatentID:")
    print(patientID)
    patient = db.getPatientDetails(patientid=patientID)
    return check(patient)  #get the id and check it.

def checkName(db, name):
    patient = db.getPatientDetails(patientsurname=name)
    return check(patient)  #get the id and check it.






    




