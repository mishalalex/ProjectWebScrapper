import requests
from bs4 import BeautifulSoup
from time import time


# to get the performance of the request
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} seconds')
        return result

    return wrapper()


@performance
def GetMeEachMonth():
    # initializing the file writer
    with open('newsarticles.txt', mode='a') as my_file:

        # go to the website, parse it, and get the data relevant to all the months in the year 2020
        res1 = requests.get('https://www.thehindu.com/archive/print/2010/',
                            headers={'Accept-Encoding': 'gzip,deflate', 'Accept': 'text,json'})
        year = BeautifulSoup(res1.text, 'html.parser')
        allmonths = year.select('#archiveWebContainer > div.archiveBorder > ul:nth-child(6) > li > a')

        # There are 12 months; go to each month page and get the links to the days within that month
        for onemonth in allmonths:
            print(f'This is the data for the month of {onemonth.getText()}')
            eachmonth = onemonth.get('href', None)
            res2 = requests.get(eachmonth)
            monthdata = BeautifulSoup(res2.text, 'html.parser')
            alldays = monthdata.select('.ui-state-default')

            # There are 28-31 days in a month; go to each day page and get the links within that day
            for oneday in alldays:
                print(f'This is the data for day - {oneday.getText()}')
                eachday = oneday.get('href', None)
                article = requests.get(eachday)

                each_date = BeautifulSoup(article.text, 'html.parser')
                alllinks = each_date.select('.archive-list > li > a')

                # Write the link text and the link to each line, one by one to a text file using a for loop
                for onelink in alllinks:
                    my_file.write(f"{onelink.getText()}|{onelink.get('href', None)}")
                    my_file.write('\n')

