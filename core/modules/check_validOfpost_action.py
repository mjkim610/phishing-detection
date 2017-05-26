from bs4 import BeautifulSoup
import urllib

def check_validOfpost_action(resp):
	mod = 'check_validOfpost_action'
	answer = "U"
	
	soup = BeautifulSoup(resp.text, 'lxml')
	found = soup.find_all('form', method = "post")
	
	for action in found:
		if "php" in action['action']:
			answer = "p"
		else:
			answer = "S"
	
	return answer, mod
