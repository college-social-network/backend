class sqlQueries:
    
    ##create sql connection
    
    
    def userIdToFollwingUN(self, userid):
        
        # return list of usernames - string
        
    def userIdToFollwingUID(self, userid):
        
        # return list of userids - int
        
    def userIdToFollwersUN(self, userid):
        
        # return list of usernames - string
    def userIdToFollwersUID(self, userid):
        
        # return list of userids - int
        
    def getUserIdSchedule(self, userid):
        
        # return json of users full schedule
     
    def getUserIdScheduleCurrDay(self, userid):
        
        # return json of users current days schedule
           
    
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<userid>/following/username', methods=['GET'])
def get_books(userid):
    return UserIdToFollwingUN(userid)
    #return list of usernames
    
@app.route('/<userid>/following/userid', methods=['GET'])
def get_books(userid):
    return UserIdToFollwingUID(userid)
    #return list of usernames

@app.route('/<userid>/followers/username', methods=['GET'])
def get_books(userid):
    return UserIdToFollwersUN(userid)
    #return list of usernames
    
@app.route('/<userid>/followers/userid', methods=['GET'])
def get_books(userid):
    return UserIdToFollwersUID(userid)
    #return list of usernames

@app.route('/<userid>/schedule/full', methods=['GET'])
def get_books(userid):
    return getUserIdSchedule(userid)
    #return list of usernames

@app.route('/<userid>/schedule/currday', methods=['GET'])
def get_books(userid):
    return getUserIdScheduleCurrDay(userid)
    #return list of usernames


if __name__ == '__main__':
    app.run(debug=True)
