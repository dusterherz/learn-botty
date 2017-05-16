from datetime import datetime
from geopy.geocoders import Nominatim
from dateutil import parser
import requests
import settings
import apiaiWebhookSerializer


def handle(response):
    lat = '50.6292500'
    lng = '3.0572560'
    # Take only the last location
    print(response.result.parameters)
    if response.result.parameters.city != '':
        geolocator = Nominatim()
        location = geolocator.geocode(response.result.parameters.city)
        lat = str(location.latitude)
        lng = str(location.longitude)
    if response.result.parameters.date != '':
        date = parser.parse(response.result.parameters.date)
    else:
        date = datetime.today()
    date.replace(hour=9, minute=0, second=0, microsecond=0)
    print(lat + ', lng : ' + lng)
    # Use of DarkSkyApi to get the meteo. Change API if the date is today
    result = requests.get('https://api.darksky.net/forecast/' +
                          settings.config['darkSky']['apiKey'] +
                          '/' + lat + ',' + lng + '?lang=fr').json()

    return apiaiWebhookSerializer.Response(result['daily']['data'][0]['summary'],
                                           result['daily']['data'][0]['summary'],
                                           response.result.source)
