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
from operator import itemgetter
import csv
import json

from collections import OrderedDict
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
            #print( row )
            #print( row[ "name" ], row[ "email" ], row[ "score" ] )
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

 
    return "POST COMPLETE"

@app.route('/Update/', methods=['PUT'])
def UpdateFile():
    max = 10
    myFlag = False
    JSON = request.get_json()
    RankList = []
    '''
    Ranking = JSON["Rankings"]
    RankList = []
    for i in Ranking:
        Name = i[ "Name" ]
        Email = i[ "Unique Email" ]
        Score = i[ "Score" ]
        Row = [ Name,Email,Score]
        RankList.append(Row) '''
    Name = JSON[ "Name" ]
    Email = JSON[ "Unique Email" ]
    Score = JSON[ "Score" ]
            
    #read in the file
    with open( 'list.csv' ) as csvfile:
        reader = csv.DictReader( csvfile )
        for row in reader:
            RankList.append( dict(row) )

    lenList = len( RankList )
    print(lenList)
    print(RankList)

    for i in RankList:
        ListName = i[ "Name" ]
        ListEmail = i[ "Unique Email" ]
        ListScore = i[ "Score" ]
        print( Name, Email, Score )
        if not myFlag :
            if ( Email == ListEmail ) :
                if ( int(Score) > int(ListScore)) :
                    print( Score )
                    #print(ListScore)
                else:
                        #do nothing
                    print( "Else reached" )
            else:
                if ( int( Score ) > int(ListScore) ):
                    
                    if( lenList < max ):
                        temp = { "Name": Name, "Unique Email": Email, "Score": Score }
                        RankList.append(temp)
                        print( "check the list" )
                        myFlag = True
                    else:
                        #sort list and append to appropiate spot
                        #clip the last spot
                        temp = { "Name": Name, "Unique Email": Email, "Score": Score }
                        RankList.append(temp)
                        print( Score, '\n',"Email wasn't in the system yet" )
                        myFlag = True


    for item in RankList:
        print(item)
    RankList = RankList[:-1]
    RankList = sorted(RankList, key=lambda Ranks: int(Ranks['Score']), reverse = True)

#writes list of dictionaries to a csv type of file
    with open('list.csv', 'w') as csvfile:
        fieldnames = ['Name', 'Unique Email', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(RankList)


    return "PUT COMPLETE"


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
