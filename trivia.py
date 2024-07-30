import requests
import json
from pprint import pprint


#Api url for geogrphic questions
url = "https://opentdb.com/api.php?amount=50&category=22"   # api url for the geography questions
response = requests.get(url)
print(response)
pprint(response.json())

with open("trivia.json","w") as f:
    json.dump(response.json(),f,indent=4)