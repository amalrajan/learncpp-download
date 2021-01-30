import argparse
import os
import platform
import sys
import urllib.request

import bs4 as bs
import pdfkit


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        type=str, help="download location")
    parser.add_argument('--nopdf', action='store_true',
                        default=False, help="skip converting to pdf")
    # parser.add_argument('--combine')
    # Next release will include a combine feature.

    args = parser.parse_args()

    if args.output[-1] not in ('/', '\''):
        if user_os == 'Windows':
            args.output += "\\"
        elif user_os == 'Linux':
            args.output += "//"

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
            if 'http' not in url or 'https' not in url:
                url = "http://www.learncpp.com" + url + "\print"
            urls += (url,)

    return urls


def save_as_pdf(url, dest):
    # For saving the web page in PDF format.
    global index

    title_from_url = url.split('/')[-2].replace(' ', '_')
    title_prettified = ' '.join([i.capitalize() for i in title_from_url.split('-')])
    title = dest + str(index) + ' ' + title_prettified + '.pdf'
    options = {'cookie': [('ezCMPCookieConsent', '-1=1|1=1|2=1|3=1|4=1')]}
    pdfkit.from_url(url, title, options=options)
    index += 1


def save_as_html(url, dest):
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
        print("Downloading {} of {} ...".format(i + 1, length))

        if args.nopdf:
            try:
                save_as_html(url, dest=args.output)
            except KeyboardInterrupt:
                print("Process terminated by the user.")
                sys.exit()
            except Exception as e:
                print("Process failed.")
                print(e)
                sys.exit(1)

        else:

            if sys.platform == 'win32':
                if os.path.exists(
                        "C:\\Program Files\\wkhtmltopdf\\bin"):
                    path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
                else:
                    path_wkthmltopdf = "C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
                # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
                # ^ to be configured for Windows

            # Else, manually specify a custom path.

            try:
                save_as_pdf(url, args.output)
            except KeyboardInterrupt:
                print("Process terminated by the user.")
                sys.exit()
            except Exception as e:
                print(e)
                sys.exit(1)


if __name__ == '__main__':
    urls = None
    user_os = platform.system()
    index = 1

    if user_os == 'Windows':
        delimiter = "\\"
    else:
        delimiter = "//"

    argument_parser()
