from urllib2 import *
import requests

def main(self):
	if get_status_code(self) == 'exist':
		return	url_name_check(self)
	if get_status_code(self) == 'U':
		return get_status_code(self)

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
		#print "Safe:",url
		status = "S"

	if(url.find("@")!=-1):
		#print "phishing:",url
		status = "P"

	if(len(url)>=75):
		#print "phishing:",url
		status = "P"

	if(url[7:].find("//")):
		#print "phishing:",url
		status = "P"

	if(url[7:].find("http")):
		#print "phishing",url
		status = "P"

	return status

'''
f = open('phishing_urls.txt','r')
while True:
	line = f.readline()
	if not line: break
	url = line.rstrip()
	main(url)
'''
