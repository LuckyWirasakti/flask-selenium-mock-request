from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from json import loads
import os

app = Flask(__name__)

GOOGLE_CHROME_PATH = os.environ.get('GOOGLE_CHROME_PATH')
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')


@app.route('/')
def root():
    return 'Welcome To The Jungle'


@app.route('/scrapper')
def handler():
    options = webdriver.ChromeOptions()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/84.0.4147.125 Safari/537.36')
    wb = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    wb.get(request.args.get('url'))
    return jsonify(loads(loads(wb.find_element(by=By.TAG_NAME, value="pre").text)))
