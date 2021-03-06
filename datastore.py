import pickledb

db = pickledb.load('/var/www/SurpriseMe/realmp7data.db', False)
try:
    db.dgetall("users")
except KeyError as e:
    db.dcreate("users")
    db.dump()
#Reetahan contributed to this file and helped set up how the user would store data.
# def passData(name, preferences, time, id):
#     namepreftime = [name, preferences, time]
#     db.set(id,namepreftime)


# def returnData(id):
#     return db.get(id)

def getUserData(id):
    try:
        return db.dgetall(id)
    except KeyError as e:
        return None

def getUsers():
    try:
        return db.dkeys("users")
    except KeyError as e:
        db.dcreate("users")
        db.dump()
        return []

def addUser(id, topics):
    db.dadd("users",(id, True))
    db.dcreate(id)
    db.dadd(id,("id",id))
    db.dadd(id,("topics",topics))
    db.dump()

def setTime(id, time):
    db.dadd(id,("time", time))
    db.dump()

def getUsersByTime(time, override = False):
    users = getUsers()
    outputUsers = []
    for user in users:
        userData = getUserData(user)
        if userData["time"] == time or override:
            outputUsers.append(userData)
    return outputUsers
