import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


from main.wsgi import application

app = application