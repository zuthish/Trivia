import requests
from pprint import pprint
import json


categories_url = "https://opentdb.com/api_category.php"
response = requests.get(categories_url)
print(response)

#Getting response in json format and pretty printing it.

pprint(response.json())

# Dump the responses in a json file
with open("categories.json","w") as f:
    json.dump(response.json(),f,indent=4)