import requests
import json
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

city=input("enter the city name:")

url=f"http://api.weatherapi.com/v1/current.json?key=31b6be80342645ee924105502252507&q={city}"

r=requests.get(url) 
# print(r.text)
# print(type(r.text))
info=json.loads(r.text) #to convert str to dict we use json function


# speak(info["current"]["temp_c"])
data=(info["current"]["temp_c"])
temp=f"the temperature in {city} is {data}"
speak(temp)