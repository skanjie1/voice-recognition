import requests

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

jokes= ["" , ""]
jokes[0]= json_data["setup"]
jokes[1]= json_data["punchline"]

def joke():
    return jokes