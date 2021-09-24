import requests
import json
from pprint import pprint

cat_fact = requests.get("https://catfact.ninja/fact")

# print(cat_fact.json())

coin_desk = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
pprint(coin_desk.json())

