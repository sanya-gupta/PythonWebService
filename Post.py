import requests
import json


'''data = {
    'Name' : 'Eric',
    'Unique Email' : 'something@unr.edu',
    'Score' : 999
}
'''
data =   {
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
                "Unique Email": "helen@unr.edu",
                "Score": 175
                },
                {
                "Name": "Pat",
                "Unique Email": "pat@unr.edu",
                "Score": 120
                }
        ]
    }

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post("http://127.0.0.1:5000/Create/", data=json.dumps(data), headers=headers)
print(r.status_code, r.reason, r.text)
