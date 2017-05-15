import apiaiWebhookSerializer


def handle(response):
    if response.source == '👢':
        text = "C'est quand il pleut, les bot"

    return apiaiWebhookSeralizer.Response(text, text, response.result.source)
