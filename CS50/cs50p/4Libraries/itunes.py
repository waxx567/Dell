# Code that uses the iTunes API (Application Programming Interface) and Python
# to get information about any musician

import json
import requests
import sys

# Error check
if len(sys.argv) != 2:
    sys.exit()

# Now the opportunity to use the requests library to write some Python code that
# Is effectively pretending to be a web browser to connect to Apple's https url on their server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])