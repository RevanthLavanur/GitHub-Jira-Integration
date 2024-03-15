from flask import Flask, request
from requests.auth import HTTPBasicAuth
import json
import requests

app = Flask(__name__)

@app.route('/jira', methods=['POST'])
def jira():
    data = request.json  # Access JSON data from the request
    if "/jira" not in data["comment"]["body"]:
        return "The comments only accepts /jira", 400

    url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/issue"
    API_TOKEN = ""
    auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
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
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
