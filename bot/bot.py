# coding: utf-8

import os
import apiaiWebhookSerializer
import settings
from .intents import handle
import logging

from flask import jsonify


def bot(request):
    response = apiaiWebhookSerializer.Request(request)
    return handle(response)
