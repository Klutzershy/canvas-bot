
import requests

#This assumes you are working on Windows, change the \ to / if you are on Mac/Linux
token_file = "..\canvas_auth_token.txt"

with open(token_file,'r') as file: API_TOKEN = file.read()

result = requests.get(url="https://rowan.instructure.com/api/v1/courses/2922508/assignments?access_token={}".format(API_TOKEN))

json_results = result.json()

print(json_results)
for i in json_results:
    print(i.get("name"))
