
import json



class people:
    def __init__(self, id, username, name,schedule, major, minor, year):
        self.id = id
        self.username = username
        self.name = name
        self.schedule = schedule
        self.major = major
        self.minor = minor
        self.year = year

#add support for asyncorus and sycronus online classes(could just have in inperon/online for ones that meet on like a zoom
vs = [
    {"Monday": ["none"]},
    {"Tuesday":
         [["CS2190", "8:00-9:15"],
          ["MATH3320", "13:00-14:15"],
          ["CS2900", "14:30-15:20"]]
     },

    {"Wednesday": ["none"]},
    {"Thursday":
         [["CS2190", "8:00-9:15"],
          ["MATH3320", "13:00-14:15"],
          ["CS2900", "14:30-15:20"]]},
    {"Friday": ["none"]},
    {"Saturday": ["none"]},
    {"Sunday": ["none"]}
]
vs = """
Monday?N+
Tuesday?CS2190@8:00-9:15@Kokosing.MATH3320@13:00-14:15@McLeod.CS2900@14:30-15:20@Hays+
Wednesday?N+
Thursday?CS2190@8:00-9:15@Kokosing.MATH3320@13:00-14:15@McLeod.CS2900@14:30-15:20@Hays.BGSU1910@16:00-17:15@University Hall+
Friday?N+
Saturday?N+
Sunday?N+
Online?MATH2220"""
p1 = people(1, "vaughngugger","Vaughn Gugger", vs, "Computer Science", "Specialization in Computational Data Science", "Freshman")


p2 = people(2, "chazwilms","Chaz Wilms", "noData", "Computer Science", "Specialization in Computational Data Science", "Sophomore")

hs = """
Monday?MATH1220@10:30-11:20@Olscamp.SPAN1020@9:30-10:20@Eppler+
Tuesday?MATH1220@10:30-11:20@Olscamp+
Wednesday?MATH1220@10:30-11:20@Olscamp.SPAN1020@9:30-10:20@Eppler+
Thursday?MATH1220@10:30-11:20@Olscamp.SPAN1020@9:30-10:20@Eppler+
Friday?MATH1220@10:30-11:20@Olscamp.SPAN1020@9:30-10:20@Eppler.WS2000@11:30-12:20@Eppler+
Saturday?N+
Sunday?N+
Online?WRIT1110
"""
p3 = people(3, "halajabri", "Hala Jabri", hs, "undeclared", "undeclared", "High School Junior")
peopleClassList = [p1, p2, p3]
namesList = ["vaughngugger", "chazwilms", "halajabri"]

class sqlQueries:

    ##create sql connection


    def userIdToFollowingUN(self, userid):
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

    def getUserIdSchedule(self, userid):
        #index = namesList.index(userid)
        #return peopleClassList[index].schedule


        for i in peopleClassList:
            if i.username == userid:
                return i.schedule
        return "NO_USER"


        # return json of users full schedule

    def getUserIdScheduleCurrDay(self, userid):
        return 30300303
        # return json of users current days schedule

    def userData(self, username):
        #print(username)
        #print(namesList)

        for i in peopleClassList:
            if i.username == username:
                return ({ "major": i.major,  "minor": i.minor, "year" : i.year, "name" : i.name})
        return "NO_USER"

        #index = namesList.index(username)
        #return ({ "major": peopleClassList[index].major,  "minor": peopleClassList[index].minor, "year" : peopleClassList[index].year, "name" : peopleClassList[index].name})


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

@app.route('/userdata/<username>', methods=['GET'])
def userData(username):
    return cl.userData(username)
    # return list of usernames

if __name__ == '__main__':
    app.run(debug=True)
