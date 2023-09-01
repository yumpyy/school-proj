import requests
from bs4 import BeautifulSoup
import os
import re

# query = "save it for parts"

def yt(query):
    # print(query)
    r = requests.get(f"https://inv.vern.cc/search?q={query}")
    
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)
    x = soup.find('div', class_='icon-buttons')
    
    link = str(x.find('a')).split('"')[1]
    # print(link)

    shell_command = f"mpv --no-video --save-position-on-quit {link}"
    # print(shell_command)
    return shell_command

# yt(query)
