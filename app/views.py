from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
from django.shortcuts import HttpResponse
load_dotenv()
# Create your views here.

# try:
def index(request):
    city = request.GET.get("city")
    api_key=os.getenv("api_key")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    api = requests.get(api_url).json()

    # name = requests.get(api_url).json()
    # if city in api['name'] and country in api['sys']["country"] :
    temp = api['main']['temp']
    city = api['name']
    country = api['sys']['country']

    allurl = {'city':city,'temp':temp,"country":country}
    return render(request,"index.html",allurl) 
# except ValueError as e:
#     print("no city name")