import apiaiWebhookSerializer


def handle(response):
    print('easter egg !')
    if response.result.resolvedQuery == '👢':
        text = "C'est quand il pleut, les bot"
    else:
        text = "🐣"
    return apiaiWebhookSerializer.Response(text, text, response.result.source)
