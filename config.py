"""
Configuration file, config is set through class rather than individually in __init__,py
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Database URI depends on environment the program is run in
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key_to_change'
    #Allows CORS
    CORS_HEADERS = 'Content-Type'