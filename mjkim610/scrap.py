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

"""
# -----------------------------------
#             FUNCTIONS
# -----------------------------------
"""
def main():
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
        writeFile.write("id,is_naver\n") # need to make file spliced by some other character? or will comma be okay

        id = 0
        is_naver = 0

        for url in phishing_urls:
            url = url.rstrip()
            print("Analyzing " + url + "...")
            try:
                current_page = (requests.get(url).text, 'lxml')

                if "naver.com" in url:
                    is_naver = 1
                else:
                    is_naver = 0
            except requests.exceptions.ConnectionError:
                print("Connection error. Check URL.")
                is_naver = -1

            writeFile.write(str(id) + "," + str(is_naver) + "\n")
            id += 1
            #sleep(1)
    print("Finished analysis!")


"""
# -----------------------------------
#         CALL MAIN FUNCTION
# -----------------------------------
"""
main()