#!/usr/bin/python
from selenium import webdriver
import argparse
import time

def screenshotSub(screenshot_url):
    br = webdriver.PhantomJS()
    timestamp = time.strftime("%s")
    br.get("http://" + str(screenshot_url))
    br.save_screenshot('/tmp/' + str(screenshot_url) + '_' + timestamp + '.png')
    br.quit

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--screenshot", help="Take a screenshot of a webpage. Already assumes 'http://' EG: snapshot.py -s <url>")
args = parser.parse_args()

if args.screenshot:
    screenshotSub(args.screenshot)

