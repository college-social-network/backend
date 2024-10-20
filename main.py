
class people:
    def __init__(self, id, username, schedule):
        self.id = id
        self.username = username
        self.schedule = schedule



p1 = people(1, "vaughnGugger", "noData")
p2 = people(2, "chazWilms", "noData")
peopleClassList = [p1, p2]
namesList = ["vaughnGugger", "chazWilms"]

class sqlQueries:

    ##create sql connection


    def userIdToFollowingUN(self, userid):
        return "|".join(namesList)
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

    def getUserIdSchedule(self, userid):
        index = namesList.index(userid)
        return peopleClassList[index].schedule
        # return json of users full schedule

    def getUserIdScheduleCurrDay(self, userid):
        return 30300303
        # return json of users current days schedule


from flask import Flask, jsonify
import json

app = Flask(__name__)

cl = sqlQueries()


@app.route('/following/username/<userid>', methods=['GET'])
def userIdToFollowingUN(userid):
    return cl.userIdToFollowingUN(userid)
    # return list of usernames


@app.route('/following/userid/<userid>', methods=['GET'])
def UserIdToFollowingUID(userid):
    return cl.UserIdToFollowingUID(userid)
    # return list of usernames


@app.route('/followers/username/<userid>', methods=['GET'])
def UserIdToFollowersUN(userid):
    return cl.UserIdToFollowersUN(userid)
    # return list of usernames


@app.route('/followers/userid/<userid>', methods=['GET'])
def UserIdToFollowersUID(userid):
    return cl.UserIdToFollowersUID(userid)
    # return list of usernames


@app.route('/schedule/full/<userid>', methods=['GET'])
def getUserIdSchedule(userid):
    return cl.getUserIdSchedule(userid)
    # return list of usernames


@app.route('/schedule/currday/<userid>', methods=['GET'])
def getUserIdScheduleCurrDay(userid):
    return cl.getUserIdScheduleCurrDay(userid)
    # return list of usernames


if __name__ == '__main__':
    app.run(debug=True)
