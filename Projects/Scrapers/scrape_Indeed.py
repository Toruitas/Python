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
from multiprocessing.pool import ThreadPool as Pool
import requests
import csv
import datetime

def scrape_all(url,limit=1000):
    """
    Recursive.
    Scrapes all pages up to limit. -1 indicates scrapes forever.
    Can't take advantage of robots, unfortunately.
    Could modify to scrape the next 3 pages, and grab the "next" from the third one.
    :param url: url to scrape
    :param limit:
    :return:
    """
    soup = scrape_one(url)
    max_results = soup.select('#searchCount')[0].get_text().split(" ")[-1].replace(",","")
    results_start = 10
    url_list = []
    if int(max_results) > limit:
        max_results = limit
    else:
        pass
    while results_start < max_results:
        url_list.append(START+"&start={}".format(results_start))
        results_start +=10
    assign_bots(url_list)
    # for url in url_list:
    #     scrape_one(url)


def scrape_all_recursive(url,limit=-1):
    """
    Recursive.
    Scrapes all pages up to limit. -1 indicates scrapes forever.
    Can't take advantage of robots, unfortunately.
    Could modify to scrape the next 3 pages, and grab the "next" from the third one.
    :param url: url to scrape
    :param limit:
    :return:
    """
    soup = scrape_one(url)
    #link = a.attrs.get('href')
    #pages = soup.select("div.pagination")  # last child of pagination links
    pages = soup.select('.pagination > a')
    #print([page.attrs['href'] for page in pages])
    #next = pages[-1]
    next_page = (pages[-1].attrs['href'])
    #next2 = (pages[-1].attrs)
    #print(pages[-1].get_text())
    next_pages_list = [BASE+next_page]
    for page in pages:
        if page.attrs['href'] > next_page:
            next_pages_list.append(BASE + page.attrs['href'])
     # if too many pages for limit, only do the first n items in list

    if "Next" not in pages[-1].get_text() or limit == 0:
        print("End of the line")
    elif len(next_pages_list) >= limit > 0:
        next_pages_list = next_pages_list[:limit-1]
        print(next_pages_list)
        # robots for that many
        assign_bots(next_pages_list)
    else:  # compare next url to numbered URLs. If different, add to list. Split on =.
        # robots for all
        assign_bots(next_pages_list[:-1])
        scrape_all_recursive(BASE+next_pages_list[-1], limit-len(next_pages_list))
        # print("Next page, coming up.")
        # skips to last page in pages list, and accounts for that wrt the limit in the next call, subtracting as
        # many items are in the next pages list from the limit



def scrape_one(url):
    response = requests.get(url)
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
        # try:
        #     with open('Indeed_scraped_{}.csv'.format(datetime.date.today()),'a', newline='', encoding='utf-8') as csvfile:
        #         writer = csv.writer(csvfile)
        #         writer.writerow([company.get_text(),position.get_text(),location.get_text()])
        # except:
        #     print("Failed to write to CSV.")

    #return [i for i in soup.find_all('div',class_="result")]
    print("scraped page {}".format(url))
    return soup

def assign_bots(urls):
    pool = Pool(8)  # 8 worker bots, generally want to use double the amount of cores you have. In this case, 8.
    # reduced to 4 for politeness and not bannyness, and since we won't need more than that
    pool.map(scrape_one,urls)

if __name__=="__main__":
    START = "http://www.indeed.com/jobs?q=%22Salesforce%22&sort=date"
    BASE = "http://www.indeed.com"
    LIMIT = 500  # page limit
    scrape_all(START,LIMIT)