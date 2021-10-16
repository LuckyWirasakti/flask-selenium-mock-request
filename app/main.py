from json import loads

from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.config import (
    CHROMEDRIVER_PATH,
    GOOGLE_CHROME_PATH
)

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome To The Jungle'


@app.route('/scrapper')
def handler():
    options = webdriver.ChromeOptions()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/84.0.4147.125 Safari/537.36'
    )
    wb = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        options=options
    )
    try:
        wb.get(request.args.get('url'))
        return jsonify(
            loads(
                loads(
                    wb.find_element(by=By.TAG_NAME, value="pre").text
                )
            )
        )
    except Exception as e:
        return str(e)
