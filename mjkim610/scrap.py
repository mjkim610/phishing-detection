#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import httplib
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime

"""
# -----------------------------------
#             CONSTANTS
# -----------------------------------
"""
URL = 'http://220.230.122.163/'
START = 'api/start'
STOP = 'api/stop'
KEY = 'user_cat'

"""
# -----------------------------------
#             FUNCTIONS
# -----------------------------------
"""
def main():
    #res = requests.post(URL + START, json={'key': KEY, 'type': "N"})
    #print(res.text)
    phishing_urls = read_list()
    get_features(phishing_urls)

def read_list():
    print("Reading list...")
    with open('phishing_list.txt', 'r') as read_file:
        phishing_urls = read_file.readlines()

    return phishing_urls

def get_features(phishing_urls):
    print("Starting analysis...")

    with open('results.txt', 'w') as writeFile:
        # Write header
        writeFile.write("id,can_access,has_keyword_naver,is_naver_domain\n")

        id = 0
        can_access = 0
        has_keyword_naver = 0
        is_naver_domain = 0

        for url in phishing_urls:
            url = url.rstrip()
            print("Analyzing " + url + "...")

            # Check can_access
            try:
                current_page = (requests.get(url).text, 'lxml')
                can_access = 1
            except requests.exceptions.ConnectionError:
                print("Connection error. Check URL.")
                can_access = 0

            # Check has_keyword_naver.com
            if "naver.com" in url:
                has_keyword_naver = 1
            else:
                has_keyword_naver = 0

            # Check is_naver_domain
            temp = url.index("/")
            try:
                temp = url[temp+2:].index("/") + temp+2
            except:
                temp = len(url) + temp+2

            url_parsed = url[:temp]
            domain_end = temp

            temp = url_parsed.rfind('.')
            domain_start = url_parsed[:temp].rfind('.')
            if domain_start == -1:
                domain_start = url_parsed[:temp].rfind('/')
            domain = url[domain_start+1:domain_end]
            print(domain)

            if domain == "naver.com":
                is_naver_domain = 1
            else:
                is_naver_domain = 0

            writeFile.write(str(id) + "," + str(can_access) + "," + str(has_keyword_naver) + "," + str(is_naver_domain) + "\n")
            id += 1
            #sleep(1)
    print("Finished analysis!")


"""
# -----------------------------------
#         CALL MAIN FUNCTION
# -----------------------------------
"""
main()