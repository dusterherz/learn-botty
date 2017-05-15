import apiaiWebhookSerializer

from .weather import handle as weatherHandle
from .easter_egg import handle as eastereggHandle


def handle(response):
    handle = {
     'meteo': weatherHandle,
     'easteregg': eastereggHandle
    }
    if response.result.action in handle:
        answer = handle[response.result.action](response)
    else:
        answer = apiaiWebhookSeralizer.Response(response.result.messages.speech,
                                                response.result.messages.speech,
                                                response.result.source)
    return answer
