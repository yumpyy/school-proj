import requests

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

wttr()
