"""
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to
create a calculator application that has use in your life. It might be an interest calculator, or it might be something
that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also
A = F/M, and M = F/A!

http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

Ideas:
1. foreign exchange calculator, based on website info
delete existing csv and download new one - updating
Currency matrix creation?
Do the DL/replace daily.
Resources:

For CSV reading:
http://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
http://java.dzone.com/articles/python-101-reading-and-writing
http://stackoverflow.com/questions/16503560/read-specific-columns-from-csv-file-with-python-csv
http://stackoverflow.com/questions/181990/programmatically-access-currency-exchange-rates
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
https://docs.python.org/3.4/library/csv.html#csv.DictReader
http://stackoverflow.com/questions/3139879/how-do-i-get-currency-exchange-rates-via-an-api-such-as-google-finance/8391430#8391430
https://code.google.com/p/yahoo-finance-managed/wiki/csvQuotesDownload
https://docs.python.org/3.4/library/csv.html

For downloading:
http://docs.python-requests.org/en/latest/user/quickstart/
http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
http://stackoverflow.com/questions/14114729/save-a-file-using-the-python-requests-library
http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
http://stackoverflow.com/questions/10283053/downloading-a-csv-file-from-the-web-with-redirects-in-python
http://stackoverflow.com/questions/21500918/download-a-csv-file-with-python
http://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-python
https://docs.python.org/3.4/library/urllib.html#module-urllib
https://docs.python.org/3.4/library/urllib.request.html#urllib.request.Request
http://stackoverflow.com/questions/7603044/how-to-download-a-file-returned-indirectly-from-html-form-submission-pyt
http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python?lq=1

Download link here: http://download.finance.yahoo.com/d/quotes.csv?s=USDEUR=X,USDAUD=X,USDCAD=X,USDJPY=X,USDGBP=X,USDCHF=X,USDHKD=X,USDINR=X,USDAED=X,USDMYR=X,USDCNY=X,USDTHB=X,USDCLP=X,USDCZK=X,USDDKK=X,USDFJD=X,USDHUF=X,USDIDR=X,USDILS=X,USDKRW=X,USDMXN=X,USDNZD=X,USDPHP=X,USDRUB=X,USDSGD=X,USDSEK=X,USDTWD=X,USDZAR=X,USDTRY=X,USDFJD=X&f=sl1d1t1ban&e=.csv

For editing csv file:
http://cbrownley.wordpress.com/2014/03/04/the-two-rs-of-python-reading-and-writing-csv-files/ ***
http://stackoverflow.com/questions/10273640/python-import-multiple-files-to-a-single-csv-file
http://stackoverflow.com/questions/15887304/copy-select-lines-from-many-text-files-and-paste-to-new-file

Finally, the true way to do it:
http://stackoverflow.com/questions/16020858/inline-csv-file-editing-with-python
http://stackoverflow.com/questions/20347766/pythonically-add-header-to-a-csv-file

For internet connection testing:
http://stackoverflow.com/questions/3764291/checking-network-connection
http://stackoverflow.com/questions/20913411/test-if-an-internet-connection-is-present-in-python
http://stackoverflow.com/questions/17440343/python-checking-internet-connection-more-than-once
http://stackoverflow.com/questions/17304225/how-to-detect-if-computer-is-contacted-to-the-internet-with-python

2. interest calculator
3. time difference from where I am, based on gps?
4. simple calculator
5. rent vs buy like NYT calculator
"""

import csv
import requests
import os
#from bs4 import BeautifulSoup
from urllib import request
from tempfile import NamedTemporaryFile
import shutil


def download_csv(website):
    #r = requests.get(website)
    #html = request.urlopen(website)
    #url = BeautifulSoup(r).find('a')['href']
    request.urlretrieve(website, 'quotes.csv')


def rewrite_csv(csv_path):
    filename = csv_path
    tempfile = NamedTemporaryFile(mode='w+', delete=False)

    with open(filename,'r+') as readFile, tempfile: #open(tempfile,"w") as writefile
        reader = csv.reader(readFile, delimiter=',') #quotechar='"'
        writer = csv.writer(tempfile, delimiter=',') #fieldnames = ["stuff1", "stuff2", "stuff3"], for writeDict version
        headers = ['currency', 'rate', 'date', 'time', 'buy', 'sell', 'shorthand']
        writer.writerow(headers)

        for row in reader:
            writer.writerow(row)

    shutil.move(tempfile.name, filename)


def check_connectivity(url='http://www.bing.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout) #Why the underscore?
        return True
    except requests.ConnectionError:
            print("No internet connection available.")
    return False

def delete_csv():
    os.remove('quotes.csv')

def return_rate_reader_complex(csv_path, currencies):
    """
    read a csv file using csv.DictReader
    :param file_object: a csv file
    :return: desired rate
    this version tries to do conversions between all currencies listed in the csv, using comparisons with USD. Possibly inaccurate.
    Saves the USD:XXX rate and the USD:YYY rate, then returns the inverse XXX:YYY rate.
    """
    with open(csv_path) as file_object:
        reader = csv.DictReader(file_object, delimiter=',')
        rate1 = 1
        rate2 = 1
        for line in reader:
            shortsplit = line['shorthand'].split()
            if currencies[0] == shortsplit[0]: #if is USD
                rate1 = 1 #1USD = X currency
            elif currencies[0] == shortsplit[2]:
                rate1 = float(line['rate']) #1USD = X currency
            if currencies[2] == shortsplit[2]:
                rate2 = float(line['rate']) #1USD = X currency
        return rate2/rate1


def return_available_exchanges_reader(csv_path):
    """
    :param file_object: csv file
    :return:printed version of available shorthand keys
    """
    with open(csv_path) as file_object: #always have to reopen the file to loop a second time
        reader = csv.DictReader(file_object, delimiter=',')
        currencySelection = ''
        for line in reader:
            currencySelection += (line['shorthand'].split(" ")[2]) + ", "
        print(currencySelection + "and USD.")

if __name__ == '__main__':
    website = 'http://download.finance.yahoo.com/d/quotes.csv?s=USDEUR=X,USDAUD=X,USDCAD=X,USDJPY=X,USDGBP=X,USDCHF=X,' \
              'USDHKD=X,USDINR=X,USDAED=X,USDMYR=X,USDCNY=X,USDTHB=X,USDCLP=X,USDCZK=X,USDDKK=X,USDFJD=X,USDHUF=X,' \
              'USDIDR=X,USDILS=X,USDKRW=X,USDMXN=X,USDNZD=X,USDPHP=X,USDRUB=X,USDSGD=X,USDSEK=X,USDTWD=X,USDZAR=X,' \
              'USDTRY=X,USDFJD=X&f=sl1d1t1ban&e=.csv'
    csv_path = 'quotes.csv'
    if check_connectivity():
        delete_csv()
        download_csv(website)
        rewrite_csv(csv_path)
    print("We currently can process these currency conversions:")
    return_available_exchanges_reader(csv_path)
    exch = input("What conversion do you want to make?")
    qty = float(input("How much currency do you have?"))
    divided = exch.split()
    rate = return_rate_reader_complex(csv_path, divided)
    print(str(qty.__round__(2))+ " " +  divided[0] + " would be ~" + str((rate * qty).__round__(2)) + " in " + divided[2] + ".")