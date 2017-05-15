from datetime import datetime
import dateutil.parser
import requests
import settings
import apiaiWebhookSerializer

def handle(response):
    lat = '50.6292500'
    lng = '3.0572560'
    # Take only the last location
    for entity in response.entities:
        if entity.name == 'location':
            lat = str(entity.lat)
            lng = str(entity.lng)
    if 'datetime' in response.entities:
        date = dateutils.parser.parse(response.entities.datetime[0].iso)
    else:
        date = datetime.today()
    date.replace(hour=9, minute=0, second=0, microsecond=0)
    print(lat + ', lng : ' + lng)
    # Use of DarkSkyApi to get the meteo. Change API if the date is today
    result = requests.get('https://api.darksky.net/forecast/' +
                          settings.config['darkSky']['apiKey'] +
                          '/' + lat + ',' + lng + '?lang=fr').json()

    return apiaiWebhookSerializer.Result(result['daily']['data'][0]['summary'],
                                         result['daily']['data'][0]['summary'],
                                         response.result.source)
