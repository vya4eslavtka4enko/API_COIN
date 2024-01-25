import os
from requests import Request,Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def sort_data(data):
    print(data)
    # for item in data:
    #      print(item)
        # if item['name'] == Chiliz:

# Rsponse

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info/'
api = os.environ['API_KEY']

session = Session()
headers = {
    "Accepts": 'application/json',
    "X-CMC_PRO_API_KEY": api
}
try:
    response = session.get(url,headers=headers)
    data = json.loads(response.text)
    sort_data(data)
except(ConnectionError,Timeout,TooManyRedirects) as e:
    print(e)

