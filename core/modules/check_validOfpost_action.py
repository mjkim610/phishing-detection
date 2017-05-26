from bs4 import BeautifulSoup

def check_validOfpost_action(resp):
	mod = 'check_validOfpost_action'
	answer = "U"
	
	soup = BeautifulSoup(resp.text, 'lxml')
	found = soup.find_all('form', method = "post")
	
	if len(found) == 0:
		return answer
	else:
		for action in found:
			#if not (action['action']):
			if "php" in action['action']:
				answer = "p"
			else:
				answer = "S"
				
		return answer, mod
