""" Checks symptoms of a patiant to see if they have anthrax or not """


def check(patiant):
    """Takes a patiant object and checks it for symptoms"""
    return False

def checkID(db,id):
    """ Checks if the patiant has anthrax, sets that status in the DB, and returns true or false """
    patiant = db.getpatiantdetails(id=id)
    return check(patiant)  #get the id and check it.

def checkName(db, name):
    patiant = db.getpatiantdetails(name=name)
    return check(patiant)  #get the id and check it.






    




