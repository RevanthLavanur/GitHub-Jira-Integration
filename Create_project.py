import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0yDDYp4VZmqydGycynyVXEBUdu9RrOR0hqih7XkfdSJ9JpleP8X6ESfI_FrmPlmaae1DfSYZsKTLcQ9QzD68Wigaz6zCQdibgztNaWcaI-S7QfmYoNC3Z6wHqipe2dngbxTKgiG0ne2mQN-Znw6FbyxYceYmOg-y5wAzGlADG6gk=D96D1ABB"

auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "REV"
    },
    "issuetype": {
      "id": "10004"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))