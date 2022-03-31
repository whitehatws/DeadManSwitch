import requests
from config import Config

r = requests.post(Config.url + '/verify', json={"key": Config.secretKey})