from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import logging
import pdfkit
import time
import sys
import os


def get_urls(cooldown=0):
    '''
    Scrapes the URLs off the website.

    :param int cooldown: specify the sleep duration in seconds, between successive requests
    '''

    req = Request('http://www.learncpp.com', headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup = BeautifulSoup(sauce, 'lxml')

    urls = []
    sno = 1

    for tutorial in soup.find_all('a'):
        url = tutorial.get('href')
        if url and 'cpp-tutorial' in url:
            if 'http' not in url or 'https' not in url:
                url = "http://www.learncpp.com" + url
            urls.append((sno, url))
            sno += 1
        if cooldown:
            time.sleep(cooldown)

    return urls


def convert_to_pdf(urls, cooldown=0, recursion_depth=0):
    '''
    Converts each webpage and saves them as PDF format.

    :param List urls: a list of URLs
    :param int cooldown: cooldown time between successive downloads
    '''
    if not os.path.exists('download'):
        os.makedirs('download')
    total = len(urls)
    failed_urls = []

    for sno, url in urls:
        logging.info(f'downloading: {url}')
        filename = 'download/' + str(sno).zfill(3) + '-' + url.split('/')[-2] + '.pdf'
        options = {
            'cookie': [('ezCMPCookieConsent', '-1=1|1=1|2=1|3=1|4=1')], 'disable-javascript': None,
            'page-size': 'A4',
            'margin-top': '0',
            'margin-bottom': '0',
            'margin-left': '0',
            'margin-right': '0'
        }
        try:
            pdfkit.from_url(url, filename, options=options)
        except Exception as e:
            logging.error(f'unable to download: {url}')
            failed_urls.append(url)

        progress(sno, total)
        time.sleep(cooldown)

    if failed_urls and not recursion_depth:
        logging.warn('attempting re-download for failed URLs')
        convert_to_pdf(failed_urls, recursion_depth=1)



def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

urls = get_urls()
convert_to_pdf(urls)
