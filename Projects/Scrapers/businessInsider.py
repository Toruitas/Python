#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Stuart'

"""
http://www.businessinsider.com/morgan-stanley-best-ecommerce-companies-2013-1
http://www.businessinsider.com/morgan-stanley-best-ecommerce-companies-2013-1?op=1
Second link is 1-page.
Scrape through, get names, go to Google, enter names, then:
https://www.google.com/webhp?hl=en#newwindow=1&hl=en&q=nordstrom+rack
First result


http://ecombd.net/2015/02/top-ten-e-commerce-companies-in-the-world/
http://fortune.com/fortune500/2011/
http://www.forbes.com/fdc/welcome_mjx.shtml
https://www.internetretailer.com/hot100/
"""

from bs4 import BeautifulSoup
import requests
import urllib.parse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

def scrape_BI(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    companies = soup.find_all('h3', class_='slide-title')
    names = []
    driver = init_driver()
    for company in companies[:]:
        name = company.getText().strip()
        # if " " in name:
        #     name.replace(' ','+')
        html_code = load_google(driver, name)
        #name, address = scrape_google(html_code)
        url = scrape_google(html_code)
        print(name,url)
        #names.append(name)
    driver.quit()
    #print(names)

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def load_google(driver,name):
    """
    Pulls the h3 class=r (first result's) data-href out.
    Again, must use selenium.
    Google API client not an option for distribution.
    :param name: queried name
    :return: html line including link and name
    """
    # url = urllib.parse.urljoin("https://www.google.com/webhp?hl=en#newwindow=1&hl=en&q=",name)
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text)
    # print(soup)

    driver.get('http://www.google.com')
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME,'q')
        ))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME,'btnK')
        ))
        box.send_keys(name)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located(
                (By.NAME,'btnG')
            ))
            button.click()
    except TimeoutException:
        print("Box or Button not found in Google.com")
    else:
        result_found = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME,'r')
        ))
        content = driver.find_element_by_css_selector("h3.r").get_attribute('innerHTML') #'innerHTML' 'h3.r'
        #print(content)
        return content

def scrape_google(html_content):
    """
    Takes the html_content of the first search result, and processes it with BS to grab the company name and url.
    Returns to the loop for now, but can just print or add to CSV
    :param html_content: html string
    :return company_name: string name of company - don't return since it's not the true name, actually a blurb
    :return url: company website url
    """
    soup = BeautifulSoup(html_content)
    tag = soup.a
    company_name = tag.get_text()
    url = tag['href']
    #print(company_name,url)
    #return company_name, url
    return url


if __name__ == "__main__":
    slideshow_url = "http://www.businessinsider.com/morgan-stanley-best-ecommerce-companies-2013-1"
    one_page_url = urllib.parse.urljoin(slideshow_url,"?op=1")
    scrape_BI(one_page_url)
    #driver = init_driver()
    #load_google(driver,"bloomberg")
    # html_content = """
    # <a href="http://www.bloomberg.com/" onmousedown="return rwt(this,'','','','1','AFQjCNH8MzYCUM46gte23HVw7JNAM_yCHg','','0CB4QFjAA','','',event)">Bloomberg Business</a>
    # """
    # scrape_google(html_content)