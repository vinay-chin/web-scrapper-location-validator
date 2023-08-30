from bs4 import BeautifulSoup
import json
from pathlib import Path
from django.shortcuts import HttpResponse, redirect, render
from LocationValidatorDjango.settings import api_key
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views import View
from environs import Env
import ssl
from datetime import datetime
from .models import scrapper, location
import urllib.request, urllib.parse, urllib.error
BASE_DIR = Path(__file__).resolve().parent.parent
import requests
from requests.structures import CaseInsensitiveDict
import googlemaps
gmaps = googlemaps.Client(key=api_key)

def home(request):
    try:
        scrapy = scrapper.objects.all()[0]
        last_updated = scrapy.last_updated    
    except:
        last_updated = "Not updated"
    return render(request, "home.html", {"last_updated":last_updated})

def scrap(request):
    latitudes = []
    longitudes = []
    page_url = 'https://www.shoppersstop.com/store-finder'
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    rawpage = requests.get(page_url,headers=headers)
    soup = BeautifulSoup(rawpage.content, 'html.parser')
    div_element = soup.find('div', {'id': 'map_canvas', 'data-stores': True})
    if div_element:
        scrap = scrapper()
        scrap.save()
        data_stores = div_element['data-stores']
        data_stores = json.loads(data_stores)
        for store in data_stores['data']:
            latitude = store['latitude']
            id = store['id']
            longitude = store['longitude']
            name = store['name']
            try:
                loc = location.objects.get(id=id)
                loc.id = id
                loc.latitude = latitude
                loc.longitude = longitude
                loc.name = name
                loc.save()
            except:
                loc = location()
                loc.id = id
                loc.latitude = latitude
                loc.longitude = longitude
                loc.name = name
                loc.save()
            print("Latitude:", latitude)
            print("Longitude:", longitude)
            print("Name:", name)
            print()
    else:
        print("Div element not found")
        messages.success(request,"unsuccessfully")
    messages.success(request,"successfully added the scrapped locations in the database!")
    return redirect("/")

def results(request):
    locations = location.objects.all()
    return render(request, "results.html", {"locations":locations})

def validate_address(latitude, longitude, name, id):
    loc = location.objects.get(id=id)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    if reverse_geocode_result:
        formatted_address = reverse_geocode_result[0]['formatted_address']
        print(f"Validated: {formatted_address}")
        loc.validate = "VALIDATED: "+formatted_address
        loc.save()
    else:
        loc.validate = "Invalid location"
        loc.save()

def validate(request):
    locations = location.objects.all()
    for item in locations:
        latitude = item.latitude
        longitude = item.longitude
        name = item.name
        id = item.id
        validate_address(latitude, longitude, name, id)   
    messages.success(request,"successfully validated the locations in the database!")
    return redirect("/results")    