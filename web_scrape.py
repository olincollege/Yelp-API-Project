import requests
from bs4 import BeautifulSoup

#requesting data from site and 
scrape = requests.get('https://symptomchecker.webmd.com/symptoms-a-z')
print(scrape)
site = "https://symptomchecker.webmd.com/symptoms-a-z"

soup = BeautifulSoup(scrape.content, 'html.parser')

findplz = soup.find_all('div', class_='list active')
print(findplz)
#this successfully scrapes symptom data (find way to make it more legible)