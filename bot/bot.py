# coding: utf-8

import os
import recastai
import settings
from .intents import handle
import logging

from flask import jsonify

def bot(payload):

  connect = recastai.Connect(token=settings.config['recast']['token'], language=settings.config['recast']['language'])
  request = recastai.Request(token=settings.config['recast']['token'])

  message = connect.parse_message(payload)

  response = request.converse_text(message.content, conversation_token=message.sender_id)

  replies = handle(response)
  connect.send_message(replies, message.conversation_id)

  return jsonify(status=200)
