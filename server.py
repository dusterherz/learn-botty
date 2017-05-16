# coding: utf-8

import os
import settings

from flask import Flask, request
from bot import bot


app = Flask(__name__)
settings.init()


@app.route("/", methods=['POST'])
def root():
    response = bot(request.data)
    print(response.format())
    return response.format()

if __name__ == '__main__':
    app.run(port=settings.config['flask']['port'])
