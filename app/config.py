import os

GOOGLE_CHROME_PATH = os.environ.get('GOOGLE_CHROME_SHIM', None)
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', 'chromedriver')
KEY_CACHE = os.environ.get('KEY_CACHE', 'lucky')
TTL_CACHE = os.environ.get('TTL_CACHE', 300)