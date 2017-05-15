import apiaiWebhookSerializer

from .weather import handle as weatherHandle
from .easter_egg import handle as eastereggHandle


def handle(response):
    handler = {
     'Weather': weatherHandle,
     'Easter Egg': eastereggHandle
    }
    print(response.result.metadata)
    if response.result.metadata and result.metadata.intentName in handler:
        answer = handler[response.result.metadata.intentName](response)
    else:
        answer = apiaiWebhookSerializer.Response(response.result.fulfillment.speech,
                                                 response.result.fulfillment.speech,
                                                 response.result.source)
    return answer
