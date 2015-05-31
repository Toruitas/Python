#!usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'Stuart'
from bs4 import BeautifulSoup
#from multiprocessing.pool import ThreadPool as Pool
import requests
import urllib.parse
import time
import selenium

def scrape_list(url):
    """
    Scrapes list given at the seed-db url.
    Finds company name, and URL to their profile page.
    Passes this URL to scrape_company, which scrapes the profile page to find the Crunchbase page,
    and then scrapes that as well for name, and website.
    :param url: seed-db.com page
    :return:
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    list = soup.select(".table > tr")

    # if want to use bots, create a large list of URLs.
    for investor in list[1:2]:
        row = investor.select('a')
        name, link = row[0].get_text(), row[0].attrs['href']
        link = urllib.parse.urljoin(BASE,link)
        scrape_company(link)
        #print(name,link)

def scrape_company(url):
    """
    crunch base doesn't let bots on it, so after we get the deep URL, we have to use Selenium.
    :param url:
    :return:
    """
    # company = requests.get(url)
    # company_soup = BeautifulSoup(company.text).select('h4 > a')
    # deep_url,name = company_soup[0].attrs['href'], company_soup[0].get_text()
    deep_url = url
    #print(deep_url,name)
    #crunch_base_page = requests.get(deep_url)
    #crunchy_soup = BeautifulSoup(crunch_base_page.text)
    #stats = crunchy_soup.select("dl.definition-list container > dd")
    #stats = crunchy_soup.find('div', class_="definition-list")


if __name__=="__main__":
    BASE = "http://www.seed-db.com"
    urls = ["http://www.seed-db.com/investorgraph/investortable?type=companies",
            "http://www.seed-db.com/investorgraph/investortable?type=accelerators",
            "http://www.seed-db.com/investorgraph/investortable?type=rounds"]
    #for url in urls:
        #scrape_list(url)
    #url = "http://www.seed-db.com/investorgraph/investortable?type=companies"
    #scrape_list(url)
    url = "https://www.crunchbase.com/organization/y-combinator"
    scrape_company(url)