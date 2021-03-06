#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Stuart'
from bs4 import BeautifulSoup
import requests
import urllib.parse
import time
from selenium import webdriver
import csv

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

"""
http://jowanza.com/post/95252758874/using-selenium-beautiful-soup-to-scrape-ajax
http://selenium-python.readthedocs.org/en/latest/waits.html didn't use a wait cuz the site is anal about robots
As such also didn;t use EC or TimeoutException
http://stackoverflow.com/questions/11750447/performing-a-copy-and-paste-with-selenium-2
http://stackoverflow.com/questions/13960326/how-can-i-parse-a-website-using-selenium-and-beautifulsoup-in-python
http://stackoverflow.com/questions/14529849/python-scraping-javascript-using-selenium-and-beautiful-soup
http://selenium-python.readthedocs.org/en/latest/page-objects.html
http://www.marinamele.com/selenium-tutorial-web-scraping-with-selenium-and-python
https://pypi.python.org/pypi/selenium
https://selenium-python.readthedocs.org/locating-elements.html#locating-elements-by-css-selectors
https://selenium-python.readthedocs.org/locating-elements.html#locating-hyperlinks-by-link-text
https://selenium-python.readthedocs.org/page-objects.html
http://saucelabs.com/resources/selenium/css-selectors
http://shahriar.svbtle.com/the-possibly-forgotten-optional-else-in-python-try-statement
http://shahriar.svbtle.com/pythons-else-clause-in-loops
http://stackoverflow.com/questions/12325454/how-to-get-text-of-an-element-in-selenium-webdriver-via-the-python-api-without
http://stackoverflow.com/questions/7263824/get-html-source-of-webelement-in-selenium-webdriver
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes

"""

def scrape_list(url):
    """
    Scrapes list given at the seed-db url.
    Finds company name, and URL to their profile page.
    Passes this URL to scrape_company, which scrapes the profile page to find the Crunchbase page,
    and then scrapes that as well for name, and website.
    :param url: seed-db.com page
    :return: Nothing, but adds to CSV.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    list = soup.select(".table > tbody > tr")
    driver = init_driver()
    # if want to use bots, create a large list of URLs.
    for investor in list[1:2]:  # skip first row, as that's just titles. Don't skip if want titles.
        row = investor.select('a')
        name, link = row[0].get_text(), row[0].attrs['href']
        link = urllib.parse.urljoin(BASE,link)
        name, home_address = scrape_company(driver,link)
        print(name,link)
        add_to_csv(name,home_address)
    driver.quit()

def scrape_company(driver,url):
    """
    crunch base doesn't let bots on it, so after we get the deep URL, we have to use Selenium.
    :param url: profile addy on seed-db
    :param driver: driver object
    :return:name, home address of company
    """
    company = requests.get(url)
    company_soup = BeautifulSoup(company.text).select('h4 > a')
    deep_url,name = company_soup[0].attrs['href'], company_soup[0].get_text()
    print(deep_url,name)

    # using BS4 to try to get crunch base info
    # crunch_base_page = requests.get(deep_url)
    # crunchy_soup = BeautifulSoup(crunch_base_page.text)
    # stats = crunchy_soup.select("dl.definition-list container > dd")
    # stats = crunchy_soup.find('div', class_="definition-list")

    # using selenium
    final_url = grab_company_address(driver,deep_url)
    return name, final_url

def init_driver():
    """
    Initializes firefox driver.
    :return: driver object
    """
    driver = webdriver.Firefox()
    # driver.wait = WebDriverWait(driver,45)
    # driver.wait = WebDriverWait(driver,45).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR,"div.definition-list.container"))
    # )
    return driver

def grab_company_address(driver,url):
    """
    Loads CrunchBase in firefox with selenium, loads the full page source, grabs the div we want, and strips out
    the url
    :param driver: firefox driver object
    :param url: crunch base company profile url
    :return: company urls
    """
    print("grabbing company address: {}".format(url))
    driver.get(url)
    time.sleep(45)  # long sleep because this site is anal about robots
    # content = driver.find_element_by_class_name('definition-list container')
    html_page = driver.page_source
    crunchy_soup = BeautifulSoup(html_page,'html5lib')
    box = crunchy_soup.select('div.definition-list.container')
    # print(box)
    website_text = box[0].find('dt',text='Website:')
    home_address = website_text.next_sibling.get_text()
    print(home_address)
    return home_address
    # print(content.getText())
    # box = driver.wait.until(EC.presence_of_element_located(()))

def add_to_csv(name, home_address):
    """
    Adds company name and address to csv file
    :param name: string name for company
    :param home_address: string url for company
    :return: nothing
    """
    with open('seed-db.csv','a',newline='') as csvfile:
        #fieldnames = ['Company Name','Homepage']
        writer = csv.writer(csvfile)
        writer.writerow([name,home_address])



if __name__=="__main__":
    BASE = "http://www.seed-db.com"
    urls = ["http://www.seed-db.com/investorgraph/investortable?type=companies",
            "http://www.seed-db.com/investorgraph/investortable?type=accelerators",
            "http://www.seed-db.com/investorgraph/investortable?type=rounds"]
    for url in urls:
        scrape_list(url)

    # add_to_csv('Didi Dache','http://www.xiaojukeji.com')
    # url = "http://www.seed-db.com/investorgraph/investortable?type=companies"
    # scrape_list(url)
    # url = "https://www.crunchbase.com/organization/y-combinator"
    # url = "https://www.crunchbase.com/organization/didi-dache"
    # url = "http://jowanza.com/post/95252758874/using-selenium-beautiful-soup-to-scrape-ajax"
    # scrape_company(url)
