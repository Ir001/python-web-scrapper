import requests
import sys
import json
from bs4 import BeautifulSoup

URL = 'https://www.jobs.id/lowongan-kerja'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='job-ads-container')
job_elems =  results.find_all('div', class_='single-job-ads')

for job_elem in job_elems:
    logo = job_elem.find('img')['src']
    job_title = job_elem.find('h3').get_text()
    job_link = job_elem.find('h3').find('a')['href']
    company = job_elem.select('p > a')[0].get_text()
    location = job_elem.select('p > span')[0].get_text()
    salary = job_elem.find_all('p')[1].get_text()
    """ Detail Page """    
    page_job = requests.get(job_link)
    content = BeautifulSoup(page_job.content, 'html.parser')
    page_detail = content.find('div', class_='job-detail')
    job_requirement = page_detail.find('div', class_='job_req')
    job_description = page_detail.find('div', class_='job_desc')
    top_panel = page_detail.find_all('div', class_='row')
    experience = top_panel[0].find('h4').find('span').get_text()
    category = top_panel[0].find_all('h4')[1].find('a').get_text()
    posted_at = top_panel[3].find_all('p')[0].get_text("",strip=True)
    deadline = top_panel[3].find_all('p')[1].get_text()
    about_company = content.find_all('div',class_='about-company')[1].get_text()
    company_panel = content.find('div',class_='company-profile').find('div',class_='panel-body')
    industry = company_panel.find_all('p')[0].find('span').get_text()
    size_company = company_panel.find_all('p')[1].find('b').get_text()
    office_address = company_panel.find_all('p')[2].find('b').get_text()
    
    link_apply = content.find('div',class_='modal-modren').find('form').attrs['action']
    
    postobj = [{
        'logo': logo,
        'title': job_title,
        'company': company,
        'about_company': about_company,
        'size_company': size_company,
        'office_address': office_address,
        'location':location,
        'salary': salary,
        'experience': experience,
        'requirement': job_requirement,
        'description': job_description,
        'category': category,
        'industry': industry,
        'posted_at': posted_at,
        'deadline': deadline,
        'apply': link_apply
    }]
    data = [{
        'success' : True,
        'message' : 'Wow'
    }]
    with open('data.json','w') as outfile:
        json.dump(postobj, outfile)
    # req_post = requests.post('http://python-scrapper.test/web-server.php', postobj)
    
    # print(req_post.content)    
    print('Complete')    
    sys.exit()
    