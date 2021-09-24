import requests
import json
from pprint import pprint

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/B706JY")

# print(post_codes_req.status_code)#status code
#
# print(post_codes_req.headers)#all http request headers
#
# print(post_codes_req.content)#request content
#
# print(post_codes_req.json())


json_body = json.dumps({"postcodes" : ["B70 6JY", "WS5 4BS", "B70 6JJ"]})
headers = {"Content-Type": "application/json"}

post_codes_req2 = requests.post("https://api.postcodes.io/postcodes", headers=headers,data = json_body)

pprint(post_codes_req2.json())

