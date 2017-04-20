from datetime import datetime
import dateutil.parser
import requests
import settings

def handle(response):
    if 'location' in response.entities:
        lat = response.entities.location.lat
        lng = response.entities.location.lng
    else:
        lat = '50.6292500'
        lng = '3.0572560'
    if 'datetime' in response.entities:
        date = dateutils.parser.parse(response.entities.datetime[0].iso)
    else:
        date = datetime.today()
    date.replace(hour=9, minute=0, second=0, microsecond=0)

    # Use of DarkSkyApi to get the meteo. Change API if the date is today
    result = requests.get('https://api.darksky.net/forecast/' +
        settings.config['darkSky']['apiKey'] +
        '/' + lat + ',' + lng + '?lang=fr').json()

    return [result['daily']['data'][0]['summary']]
