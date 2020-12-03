import requests
import sys
from bs4 import BeautifulSoup

URL = 'https://www.jobs.id/lowongan-kerja'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='job-ads-container')

# print(results.prettify())
job_elems =  results.find_all('div', class_='single-job-ads')

for job_elem in job_elems:
    logo = job_elem.find('img')['src']
    job_title = job_elem.find('h3').get_text()
    job_link = job_elem.find('h3').find('a')['href']
    company = job_elem.select('p > a')[0].get_text()
    location = job_elem.select('p > span')[0].get_text()
    salary = job_elem.find_all('p')[1].get_text()
    
    print(location, end='\n'*2)
    page_job = requests.get(job_link)
    content = BeautifulSoup(page_job.content, 'html.parser')
    job_description = content.find('div', class_='job_req')
    print(job_description)
    sys.exit()
    