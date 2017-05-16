from datetime import datetime
from geopy.geocoders import Nominatim
from dateutil import parser
import requests
import settings
import apiaiWebhookSerializer


def handle(response):
    lat = '50.6292500'
    lng = '3.0572560'
    # get lat and lng from the city
    if response.result.parameters.city != '':
        geolocator = Nominatim()
        location = geolocator.geocode(response.result.parameters.city)
        lat = str(location.latitude)
        lng = str(location.longitude)

    # get timestamp from the date
    if response.result.parameters.date != '':
        date = parser.parse(response.result.parameters.date)
    else:
        date = datetime.today()

    # Use of DarkSkyApi to get the meteo.
    result = requests.get('https://api.darksky.net/forecast/' +
                          settings.config['darkSky']['apiKey'] +
                          '/' + lat + ',' + lng + '?lang=fr').json()
    message = ("Je n'ai pas trouvé la météo pour cette date. "
               "La date n'est pas trop loin dans le futur ?")
    for data in result['daily']['data']:
        forecast_time = datetime.fromtimestamp(data['time'])
        if forecast_time.date() == date.date():
            message = data['summary']
    return apiaiWebhookSerializer.Response(message, message,
                                           response.result.source)
