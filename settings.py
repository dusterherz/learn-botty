import configparser

def init():
    global config
    config = configparser.ConfigParser()
    config.read('config.ini')
