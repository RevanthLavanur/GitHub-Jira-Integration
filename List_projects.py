# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", "ATATT3xFfGF0yDDYp4VZmqydGycynyVXEBUdu9RrOR0hqih7XkfdSJ9JpleP8X6ESfI_FrmPlmaae1DfSYZsKTLcQ9QzD68Wigaz6zCQdibgztNaWcaI-S7QfmYoNC3Z6wHqipe2dngbxTKgiG0ne2mQN-Znw6FbyxYceYmOg-y5wAzGlADG6gk=D96D1ABB")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
# output = json.loads(response.text)
# name = output[0]["name"]
# print(name)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))