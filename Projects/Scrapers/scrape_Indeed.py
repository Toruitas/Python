#!usr/bin/python
__author__ = 'Stuart'

"""
http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
http://stackoverflow.com/questions/26497722/scrape-multiple-pages-with-beautifulsoup-and-python
http://stackoverflow.com/questions/26727328/how-to-scrape-the-web-table-with-multiple-pages-using-r-or-python
http://stackoverflow.com/questions/10340290/python-beautifulsoup-looping-through-multiple-pages
http://www.kscottz.com/web-scraping-with-beautifulsoup-and-python/
"""

from bs4 import BeautifulSoup
import requests
import csv
import datetime

start_url = "http://www.indeed.com/jobs?q=%22Salesforce%22&sort=date"

def scrape_one(start_url):
    response = requests.get(start_url)
    soup = BeautifulSoup(response.text)

    jobs =  soup.find_all('div',class_="row result")
    print(len(jobs))

    # can definitely break this into a better method.
    for i,job in enumerate(jobs):
        start = 0
        position = None
        position_checks = [job.find('a', itemprop="title"),job.find('h2', class_="jobtitle"),job.find('a', class_="jobtitle")]
        while position == None:
            if start > len(position_checks):
                break
            try:
                position = position_checks[start]
            except:
                pass
            start +=1
        start = 0
        company = None
        company_checks = [job.find('span', itemprop="name"),job.find('span', class_="name"),
                          job.find('div', class_="company"),job.find('span',itemprop='hiringOrganization'),
                          job.find('span', class_='company')]
        while company == None:
            if start > len(company_checks):
                break
            try:
                company = company_checks[start]
            except:
                pass
            start +=1
        start = 0
        location = None
        location_checks = [job.find('span',itemprop="addressLocality"),job.find('span',class_="location")]
        while location == None:
            if start > len(location_checks):
                break
            try:
                location = location_checks[start]
            except:
                pass
            start +=1
        print(i)
        try:
            print(company.get_text(),position.get_text(),location.get_text())
        except:
            print(job.prettify())
        try:
            with open('Indeed_scraped_{}.csv'.format(datetime.date.today()),'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([company.get_text(),position.get_text(),location.get_text()])
        except:
            print("Failed to write to CSV.")

    #return [i for i in soup.find_all('div',class_="result")]
    print(soup.prettify())

#TODO: add multiple page scraping capabilities. Scrape linked page, plus go through pgs 2-10 for example

scrape_one(start_url)