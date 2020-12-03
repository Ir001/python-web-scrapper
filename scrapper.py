import requests
from bs4 import BeautifulSoup

URL = 'https://www.jobs.id/lowongan-kerja'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='job-ads-container')

print(results.prettify())