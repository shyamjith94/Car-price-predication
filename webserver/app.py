from flask import Flask
import os

# GLOBAL CONST DATA

DIR_PATH = os.path.normpath(os.getcwd() + os.sep + os.pardir) + os.sep

# CONST
app = Flask(__name__)

