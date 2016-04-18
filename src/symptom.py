""" module for loading and storing the symptom types that we load from the files """


def loadSymptoms(filenames=[("inhalation","symptoms/inhalation.json"), ("gastro","symptoms/gastro.json")]):
    """Loads all the symptoms from the files """

    symptoms = dict()   #Dict containing symptom types
    symptoms['inhalation'] = list() #List of symptom objects
    symptoms['gastro'] = list()


    for symptomFile in filenames:   #open and load the files
        symptoms[symptomFile[0]] = list()   #Create a new list and type in our dictionary
        try:
            f = open(symptomFile[1])    #Open the file
        except FileNotFoundError:
            return None

        #TODO catch file opening error

        for line in f:  #Read lines into our list of symptoms, make sure we're keeping the JSON formatting for later!
            symptoms[symptomFile[0]].append(line)  #Add it to the list of symptoms

        #repeat this for ever list of symptoms we have


    return symptoms #Return our dictionary of lists

