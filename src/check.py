""" Checks symptoms of a patient to see if they have anthrax or not """

import json as JSON
import symptom as symptomLoader
import patient as PatientMod


def check(patient):
    """Takes a patient object and checks it for symptoms"""


    symptoms = patient.patientData['Symptoms']  #Get the symptoms
    patientChanceRank = 0   #The current total ranking points the patient has

    for patientSymptoms in symptoms:    #For every symptom the patient has
        print(patientSymptoms)
        try:
            savedSymptoms = symptomLoader.loadSymptoms()
            for types in savedSymptoms.items():    #For every type of symptoms we've loaded
                for givenSymptoms in types[1]:    #For every symptom in that type
                    json = dict()   
                    
                    json = JSON.loads(givenSymptoms) #load it

                    if "total" in json: #If this is the total symptoms number, then store it!
                        totalSymptoms = int(json['total'])
                        continue    #There wont be any more info in this record

                    try:
                        name = json['name'] #TODO catch key error   #Get the fields
                        rank = json['rank'] 

                        if name.lower() == patientSymptoms['name'].lower():  #If they're equal
                            print("match")
                            patientChanceRank += rank   #Add the ranking points from that symptom
                    except KeyError:
                        print("Couldent get keys")

        except TypeError:   #Catch if loadSymptoms() returns None
            return 0
    return  patientChanceRank / totalSymptoms * 100 

def checkID(db,patientID):
    """ Checks if the patient has anthrax, sets that status in the DB, and returns true or false """
    p = PatientMod.patient(db.getPatientDetails(patientid=patientID))

    print(type(p.patientData))

    percentageChance = check(p)
#    p.patientData['percentage_chance'] = percentageChance   #Add the new data to the patient record
#    db.write(p) #Write the new record!

    #TODO We should probably write back to the DB here the chance that they got
    return percentageChance  #get the id and check it.

def checkName(db, name):
    p = PatientMod.patient(db.getPatientDetails(patientsurname=name))

    percentageChance = check(p)
    p.patientData['percentage_chance'] = percentageChance   #Add the new data to the patient record
    db.write(p) #Write the new record!

    #TODO We should probably write back to the DB here the chance that they got
    return percentageChance  #get the id and check it.
