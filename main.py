class sqlQueries:
    
    ##create sql connection
    
    
    def userIdToFollowingUN(self, userid):
        return json.dumps(["vaughnGugger", "chazWilms"])
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
        return 30300303
        # return json of users full schedule
     
    def getUserIdScheduleCurrDay(self, userid):
        return 30300303
        # return json of users current days schedule
           
    
from flask import Flask, jsonify
import json

app = Flask(__name__)

cl = sqlQueries()

@app.route('/<userid>/following/username', methods=['GET'])
def userIdToFollowingUN(userid):
    return cl.userIdToFollowingUN(userid)
    #return list of usernames
    
@app.route('/<userid>/following/userid', methods=['GET'])
def UserIdToFollowingUID(userid):
    return cl.UserIdToFollowingUID(userid)
    #return list of usernames

@app.route('/<userid>/followers/username', methods=['GET'])
def UserIdToFollowersUN(userid):
    return cl.UserIdToFollowersUN(userid)
    #return list of usernames
    
@app.route('/<userid>/followers/userid', methods=['GET'])
def UserIdToFollowersUID(userid):
    return cl.UserIdToFollowersUID(userid)
    #return list of usernames

@app.route('/<userid>/schedule/full', methods=['GET'])
def getUserIdSchedule(userid):
    return cl.getUserIdSchedule(userid)
    #return list of usernames

@app.route('/<userid>/schedule/currday', methods=['GET'])
def getUserIdScheduleCurrDay(userid):
    return cl.getUserIdScheduleCurrDay(userid)
    #return list of usernames


if __name__ == '__main__':
    app.run(debug=True)
