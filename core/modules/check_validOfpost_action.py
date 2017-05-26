from bs4 import BeautifulSoup

def check_validOfpost_action(resp):
	mod = 'check_validOfpost_action'
	answer = "U"
	
	soup = BeautifulSoup(resp.text, 'lxml')
	found = soup.find_all('form', method = "post")
	
	if len(found) == 0:
		return answer,mod
	else:
		for action in found:
			a = action.get('action')
			if a:
				if 'php' in a:
					answer = "p"
				else:
					answer = "S"
				
		return answer, mod
