# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://lavanurrevanthreddy258.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("lavanurrevanthreddy258@gmail.com", "ATATT3xFfGF0F5Jh92Fsffn1xF0DijZkZLXx78IH3h_Ylfjz4PQZS44GPn2JEGpKLUKVn5SO1S3aHkk054RrQ3hI64x7CG2Igw4q8Sk5Vizit_IODv6LOd-lSr2wROxB2ibad_b7jxxC-ncxP5O81NuySR9cEXqmSPgK9Oyar3H6vR3n-HbshgU=DA8D4FF3")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output = json.loads(response.text)
name = output[1]["name"]
print(name)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))