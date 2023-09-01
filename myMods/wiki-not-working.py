import requests
from bs4 import BeautifulSoup
import os
import re

query = "anime"

def ciki(query):
    for char in query:
        if char in " ":
            print("multi word")
        else:
            print("single word")
            query = "_".join(query)
    print(query)
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://en.wikipedia.org/wiki/{query}"

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    print(query)
    x = soup.find_all('p')
    print(x)

ciki(query)
