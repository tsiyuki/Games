import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("JOKE    LIBRARY")
header = colored(header, color = 'cyan')
print(header)

user_input = input("What would you like to search for?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url, 
	headers = {"Accept": "application/json"},
	params = {"term" : user_input}
).json()
num_jokes = res["total_jokes"]
if num_jokes > 1 :
	print(f"I found {num_jokes} jokes, here is one of them:")
	pick = choice(res['results'])
	print(pick['joke'])
elif num_jokes == 1:
	print(f'Here is one joke:')
	print(res['results'][0]['joke'])
else:
	print("There are no joke")