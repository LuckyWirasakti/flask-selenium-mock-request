from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from json import loads

app = Flask(__name__)

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'


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
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/84.0.4147.125 Safari/537.36')
    wb = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, options=options)
    wb.get('https://www.idx.co.id/umbraco/Surface/Home/GetTopValue')
    return jsonify(loads(loads(wb.find_element(by=By.TAG_NAME, value="pre").text)))