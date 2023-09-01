import requests
# query = "anime"

def word(query):
   
   headers = {'User-Agent': 'Mozilla/5.0'}
   url = f"https://api.urbandictionary.com/v0/define?term={query}"
   # print(url)
   r = requests.get(url, headers=headers)

   data = r.json()
   definition = data["list"][0]["definition"].split("\n")[0]
   # print(definition)
   return definition
