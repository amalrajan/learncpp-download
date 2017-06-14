import urllib.request
import bs4 as bs
import argparse
import pdfkit
import sys
import os


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default=os.getcwd(), type=str, help="download location?")

    args = parser.parse_args()
    sys.stdout.write(str(main(args)))

def get_urls():
    # Scrapes the URLs off the website.
    global urls

    sauce = urllib.request.urlopen("http://www.learncpp.com").read()
    soup = bs.BeautifulSoup(sauce, 'lxml')

    urls = ()

    for i in soup.find_all('a'):
        url = i.get('href')
        if url and 'cpp-tutorial' in url:
            if not 'http://' in url:
                url = "http://www.learncpp.com" + url
            urls += (url,)

    return urls


def convert_to_pdf(url):
    pass
    # Under development


def save_webpage(url, dest):
    # For saving web pages to the permanent storage media.
    data = urllib.request.urlopen(url).read()
    title = url.split('/')[-2].replace(' ', '_') + '.html'

    with open("{}\{}".format(dest, title), 'wb') as f:
        f.write(data)


def main(args):
    # Main function.
    urls = get_urls()
    length = len(urls)

    for i, url in enumerate(urls):
        print("Downloading {} of {} ...".format(i+1, length))
        try:
            save_webpage(url, dest=args.output)
        except KeyboardInterrupt:
            print("Process terminated.")
            sys.exit()
        except:
            print("Process failed.")
            sys.exit()

if __name__ == '__main__':
    argument_parser()