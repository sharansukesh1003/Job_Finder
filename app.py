from bs4 import BeautifulSoup
import time
from pip._vendor import requests
from pip._vendor.requests.api import post

print('Enter The Programming language')
entered_value = input('>')
print('Enter any one unfamiliar skill')
unfamiliar_skills = input('>')
print(f'Filtering out: {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={entered_value}&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        posted_date = job.find('span',class_='sim-posted').span.text
        if 'few' in posted_date:
            company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            job_url = job.find('h2').a['href']
            if unfamiliar_skills not in skills:
                print(f'Company Name:{company_name.strip()}')
                print(f'Required Skills:{skills.strip()}')
                print(f'Link:{job_url}')
                print(100*'-')

if __name__ == '__main__':
    while True:
        find_jobs()
        waiting_time = 10
        print(f'Next search in {waiting_time} minutes.')
        time.sleep(600)