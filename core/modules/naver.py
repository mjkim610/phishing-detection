import urllib
import urllib2
from urllib2 import *
import requests

def main(self):
	if get_status_code(self) == 'exist':
		url_name_check(self)
	if get_status_code(self) == 'U':
		print 'Unknown:', self

def get_status_code(self):
	try:
		response = requests.get(self)
		#print response.status_code
		status = "exist"
	except requests.ConnectionError, e:
		status = "U"
	return status

def url_name_check(self):
	url = self.rstrip()
	print "Now...", url
	if(url[0:7].find("https")):
		print "Safe:",url
		status = "S"

	if(url.find("@")!=-1):
		print "phishing:",url
		status = "P"

	if(len(url)>=75):
		print "phishing:",url
		status = "P"

	if(url[7:].find("//")):
		print "phishing:",url
		status = "P"

	if(url[7:].find("http")):
		print "phishing",url
		status = "P"

f = open('phishing_urls.txt','r')
while True:
	line = f.readline()
	if not line: break
	url = line.rstrip()
	main(url)

# url exist check
'''
url = "https://www.naver12ddd324s.com"
print get_status_code(url)
url2 = "https://www.naver.com"
print get_status_code(url2)
'''
'''
status = ""
f = open('phishing.txt','r');


while True:
	line = f.readline()
	if not line: break
	url = line.rstrip()
	try:
		
		if(url.find("@")!=-1):
			print "phishing:",url
			status = "P"
		if(len(url)>=75):
			print "phishing:",url
			status = "P"
		if(url[7:].find("//")):
			print "phishing:",url
			status = "P"
		if(url[0:7].find("https")):
			print "Safe"
			status = "S"
		if(url[7:].find("http")):
			print "phishing",url
			status = "P"
	except requests.exceptions.ConnectionError:
		print("Not Exist")
		status = "U"
'''