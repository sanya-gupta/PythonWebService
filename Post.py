import requests
import json


Login = {
    'Name' : 'Pat',
    'Unique Email' : 'something@unr.edu',
    'Score' : 123
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post("http://127.0.0.1:5000/Create/", data=json.dumps(Login), headers=headers)
print(r.status_code, r.reason, r.text)
