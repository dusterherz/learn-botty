#coding: utf-8

import os
import settings

from flask import Flask, request
from bot import bot


app = Flask(__name__)
settings.init()

@app.route("/", methods=['POST'])
def root():
  return bot(request)

if __name__ == '__main__':
    app.run(port=settings.config['flask']['port'])
