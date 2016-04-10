""" Patiant object  - Basically just contains the methods you might want to perform on the patiant data. So not much really! """

class patiant:

    patiantData = dict()

    def __init__(jsonPatiant):
    """ constructor, takes the dictionary of patiant data """
    return

    def setLocations(locations):
        """ Adds a locations field to the patiant data. Must be coupled manually because we want to keep them seperate really """
        return 

    def getField(field):
        """ Returns the field from patiantData. We have a specific method for this so we can catch fields that don't exist."""
        return patiantData[field]




    
    
    
    
{
    "Symptoms": [
    "address": "14 Taylor St",
    "city": "St. Stephens Ward",
    "company_name": "Alan D Rosenburg Cpa Pc",
    "county": "Kent",
    "email": "atomkiewicz@hotmail.com",
    "first_name": "Aleshia",
    "id": 1,
    "last_name": "Tomkiewicz",
    "phone1": "01835-703597",
    "phone2": "01944-369967",
    "postal": "CT2 7PP",
    "report_location": {
    },
    "report_method": "NHS111",
    "web": "http:\/\/www.alandrosenburgcpapc.co.uk"
}
