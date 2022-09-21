from os.path import join,dirname
from dotenv import load_dotenv
import sys

def load():
    ENVFILE_PATH = join( dirname(__file__), '..', '.env')
    load_dotenv(ENVFILE_PATH)