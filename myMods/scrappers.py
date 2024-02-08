import requests
from bs4 import BeautifulSoup

def wttr():

    url = "https://wttr.in/?format=j1"

    r = requests.get(url)
    data = r.json()
    # print(data)
    currentCond = data["current_condition"][0]
    weather = data["weather"][0]["hourly"][0]

    # print(currentCond)
    # print("-----")

    temp = currentCond["temp_C"]
    humidity = currentCond["humidity"]

    rainChances = weather["chanceofrain"]
    if int(rainChances) < 50:
        rainChances = f"The chances of rain is {rainChances} percent, You might not need an umbrella"
    elif int(rainChances) > 50:
        rainChances = f"The chances of rain is {rainChances} percent, Dont forget to carry an umberlla"

    final = f"Todays temperature is {temp} degree celcius, The humidity is {humidity} percent and {rainChances}"
    return final

def word(query):
   
   headers = {'User-Agent': 'Mozilla/5.0'}
   url = f"https://api.urbandictionary.com/v0/define?term={query}"
   # print(url)
   r = requests.get(url, headers=headers)

   data = r.json()
   definition = data["list"][0]["definition"].split("\n")[0]
   # print(definition)
   return definition

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

def gptRespond(query):
    shell_command = f'tgpt -q "{query}"'
    return shell_command
