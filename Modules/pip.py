import requests
from pprint import pprint

bbc = requests.get("https://www.bbc.co.uk")

pprint(bbc.headers)

