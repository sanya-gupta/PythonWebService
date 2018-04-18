# This is how commenting works in Python
''' This is a doc string, usually meant to describe functionality of a function.
    This is not for every comment line'''
# Indenting indicates a change in scope.
# For examples, in a if statement...
# if i in counter:
#   print i
# The command to print i is within the scope of the if function.
# Same thing for loops, okay? (for i in counter)
# Basically, NO INDENTING WITH SPACES!!!

# This is where you import libraries (called Modules in Python)
from flask import Flask, request, jsonify, json
import csv
import json
# This designates this file as a Flask Application
app = Flask(__name__)

# App route is the URL route. For examples, if your domain was
# http://www.SanyaGupta.cse.unr.edu, then the route would do functionality at
# http://www.SanyaGupta.cse.unr.edu/Read/ . Make sense?
@app.route('/Read/', methods=['GET'])
# This is to define a function, remember to indent after. Anything indented
# after the function is in the scope of the function.
def ReadFile():
    array = []
    with open( 'list.csv' ) as csvfile:
        reader = csv.DictReader( csvfile )
            # ourArray = list( reader )
        for row in reader:
            array.append( row )
            print( row )
            print( row[ "name" ], row[ "email" ], row[ "score" ] )
        r = json.dumps( array )
        return r

# Follow the same recipe for POST and the rest
@app.route('/Create/', methods=['POST'])
def CreateEntry():
    #Catches Json object sent to this route
    JSON = request.get_json()
    Name = JSON[ "Name" ]
    Email = JSON[ "Unique Email" ]
    Score = JSON[ "Score" ]
    print( Name, Email, Score )
    #we made a dictionary
    postData = [ [ Name , Email, Score ] ]
    print( postData )
  
  
    with open ( 'list.csv', 'w' ) as csvfile:
        #create writer object
        writer = csv.writer( csvfile )
        writer.writerows( postData )
 
    return "POST complete"

@app.route('/Update/', methods=['PUT'])
def UpdateFile():
    JSON = request.get_json()
    Name = JSON[ "Name" ]
    Email = JSON[ "Unique Email" ]
    Score = JSON[ "Score" ]
    print( Name, Email, Score )
   
   data = {
           "Rankings":[
            {
                       "Name": "Sanya",
                       "Unique Email": "sgupta@nevada.unr.edu",
                       "Score": 120
            },
            {
                       "Name": "Ryan",
                       "Unique Email": "ryan@gmail.com",
                       "Score": 0
            },
            {
                       "Name": "Vinh",
                       "Unique Email": "vinh@unr.edu",
                       "Score": 150
            },
            {
                       "Name": "Connor",
                       "Unique Email": "connor@unr.edu",
                       "Score": 149
            },
            {
                       "Name": "Hannah",
                       "Unique Email": "hannah@unr.edu",
                       "Score": 200
            },
            {
                       "Name": "Jervyn",
                       "Unique Email": "jervyn@unr.edu",
                       "Score": 122
            },
            {
                       "Name": "Sven",
                       "Unique Email": "sven@unr.edu",
                       "Score": -100
            },
            {
                       "Name": "Jake",
                       "Unique Email": "jake@unr.edu",
                       "Score": 100
            },
            {
                       "Name": "Helen",
                       "Uniqure Email": "helen@unr.edu",
                       "Score": 175
            },
            {
                       "Name": "Pat",
                       "Unique Email": "pat@unr.edu",
                       "Score": 120
            }
   ]
}
    
    jsonData = json.dumps(data)
    print(jsonData)
   
    with open ( 'list.csv', 'w' ) as csvfile:
        json.dump(data,)
    
    
    return "Crap needs updating, yo"

@app.route('/Delete/', methods=['DELETE'])
def DeleteEverything():
    return "DESTROY EVERYTHING"

if __name__ == '__main__':
    # This application unless specified runs on localhost, which means ONLY
    # your computer. This is generally for testing purposes. Specifically,
    # it runs on 127.0.0.1:5000 as a default. 5000 is the port and the rest
    # is localhost
    app.run(debug=True)

    # If you wanted to set the code to run on a domain and port, you would
    # use these two lines. Turns off the debugger and sets the domain to deploy
    #app.debug = false
	#app.run(host='127.0.0.1', port=8081)
