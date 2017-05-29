import requests

def main(self):
	result = get_status_code(self)
	if result == 'exist':
		result = url_name_check(self)
	else:
		result = "U"
	return result


def get_status_code(self):
	try:
		response = requests.get(self, timeout=3)
		status = "exist"
	except requests.ConnectionError, e:
		status = "U"
	except requests.exceptions.Timeout:
		status = "U"
	return status

def url_name_check(self):
	status = "U"
	url = self.rstrip()
	# print "Now...", url
	if(url[0:7].find("https") == 1):
		#print "Safe:",url
		status = "SL"

	if(url.find("@") != -1):
		#print "phishing:",url
		status = "P"

	if(len(url)>=75):
		#print "phishing:",url
		status = "P"

	if(url[7:].find("//") != -1):
		#print "phishing:",url
		status = "P"

	if(url[7:].find("http") != -1):
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
