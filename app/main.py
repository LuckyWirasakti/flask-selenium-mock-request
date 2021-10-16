from json import loads

from flask import Flask, jsonify, request
from flask_cacheify import init_cacheify
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.config import (
    CHROMEDRIVER_PATH, 
    GOOGLE_CHROME_PATH, 
    KEY_CACHE,
    TTL_CACHE
)

app = Flask(__name__)
cache = init_cacheify(app)


@app.route('/')
def root():
    return 'Welcome To The Jungle'


@app.route('/scrapper')
def handler():
    try:
        return cache.get(KEY_CACHE)
    except:
        options = webdriver.ChromeOptions()
        options.binary_location = GOOGLE_CHROME_PATH
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/84.0.4147.125 Safari/537.36'
        )
        wb = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH, options=options)
        try:
            wb.get(request.args.get('url'))
            cache.set(KEY_CACHE, jsonify(
                loads(loads(wb.find_element(by=By.TAG_NAME, value="pre").text))), TTL_CACHE)
            return cache.get(KEY_CACHE)
        except Exception as e:
            return str(e)
