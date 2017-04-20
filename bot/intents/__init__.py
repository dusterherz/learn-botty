from .weather import handle as weatherHandle
from .easter_egg import handle as eastereggHandle

def handle(response):
    handle = {
     'meteo': weatherHandle,
     'easteregg': eastereggHandle
    }
    if response.intents[0].slug in handle:
        replies = handle[response.intents[0].slug](response)
    else:
        replies = response.replies
    return [{'type': 'text', 'content': r} for r in replies]
