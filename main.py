import mysql.connector
from flask import Flask, jsonify


print("Backend Server Active")
app = Flask(__name__)

#Load in configuration data for accessing mysql database
configdata = open("config.txt", "r")
host = configdata.readline()
user = configdata.readline()
password = configdata.readline().rstrip("\n")
database = configdata.readline()

dbConn = mysql.connector.connect(host=host,user=user,password=password,database=database)

class people:
    def __init__(self, id, username, name,schedule, major, minor, year):
        self.id = id
        self.username = username
        self.name = name
        self.schedule = schedule
        self.major = major
        self.minor = minor
        self.year = year


#start up sequence to pull all user information from database
#better than having it stored in this file
#however it still essentially does the same thing as before
#nothing gets updated after initialization

#fetch all users from database
conn = dbConn.cursor()
conn.execute("SELECT * FROM required_user_info")
allUserData = conn.fetchall()

peopleClassList = []

#fetch schedule from db for all users through users id
for person in allUserData:
    conn.execute(f"SELECT schedule FROM schedule where id='{person[0]}'")
    peopleClassList.append(people(person[0],person[1],person[2],conn.fetchone()[0],person[5],person[6],person[7]))

#end connections to database and clean up
conn.close()
dbConn.close()
del allUserData

class sqlQueries:


    def getUserNameScheduleForDay(self, userName, daynum):
        if int(daynum) > 7:
            return "INVALID_DAYNUM"

        person = self.findPersonFromUserName(userName)

        if person[0] == 0:
            return "NO_USER"
        person = person[1]

        scheduleDaySplit = person.schedule.split('+')
        return scheduleDaySplit[int(daynum)]


    def userNameToFollowingUN(self, userid):
        a = ""
        for i in peopleClassList:
            a += (i.username + "|")
        a = a[:-1]
        return a
        #return "|".join(namesList)
        # return list of usernames - string

    def userIdToFollowingUID(self, userid):
        return 30300303
        # return list of userids - int

    def userIdToFollowersUN(self, userid):
        return 30300303
        # return list of usernames - string
    def userIdToFollowersUID(self, userid):
        return 30300303
        # return list of userids - int

    def getUserNameSchedule(self, userName):

        person = self.findPersonFromUserName(userName)
        if person[0] == 0:
            return "NO_USER"

        return person[1].schedule
        # return users full schedule

    def getUserIdScheduleCurrDay(self, userid):
        return 30300303
        # return json of users current days schedule

    def userData(self, username):

        person = self.findPersonFromUserName(username)

        if person[0] == 0:
            return "NO_USER"
        person = person[1]

        return ({ "major": person.major,  "minor": person.minor, "year" : person.year, "name" : person.name})

        #index = namesList.index(username)
        #return ({ "major": peopleClassList[index].major,  "minor": peopleClassList[index].minor, "year" : peopleClassList[index].year, "name" : peopleClassList[index].name})

    def findPersonFromUserName(self, username):
        for person in peopleClassList:
            if person.username == username:
                return [1, person]
        return [0]
    def findPersonFromId(self, userId):
        for person in peopleClassList:
            if person.id == userId:
                return [1, person]
        return [0]



cl = sqlQueries()


@app.route('/following/username/<userid>', methods=['GET'])
def userNameToFollowingUN(userid):
    return cl.userNameToFollowingUN(userid)
    # return list of usernames
@app.route('/following/userid/<userid>', methods=['GET'])
def UserIdToFollowingUID(userid):
    return cl.userIdToFollowingUID(userid)
    # return list of usernames
@app.route('/followers/username/<userid>', methods=['GET'])
def UserIdToFollowersUN(userid):
    return cl.userIdToFollowersUN(userid)
    # return list of usernames
@app.route('/followers/userid/<userid>', methods=['GET'])
def UserIdToFollowersUID(userid):
    return cl.userIdToFollowersUID(userid)
    # return list of usernames
@app.route('/schedule/full/<userid>', methods=['GET'])
def getUserNameSchedule(userid):
    return cl.getUserNameSchedule(userid)
    # return list of usernames
@app.route('/schedule/currday/<userid>', methods=['GET'])
def getUserIdScheduleCurrDay(userid):
    return cl.getUserIdScheduleCurrDay(userid)
    # return list of usernames
@app.route('/schedule/day/<userid>/<daynum>', methods=['GET'])
def getUserNameScheduleForDay(userid, daynum):
    return cl.getUserNameScheduleForDay(userid, daynum)
    # return the schedule for the day with the associated number
    # 0-6 correspond to mon-sun, and 7 is online classes
@app.route('/userdata/<username>', methods=['GET'])
def userData(username):
    return cl.userData(username)
    # return list of usernames

if __name__ == '__main__':
    app.run(debug=True)
