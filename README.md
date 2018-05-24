# www.learncpp.com Website Crawler

_The primary aim is demonstrate how to fetch tutorials from www.learncpp.com and store them in PDF format for offline viewing using Python._

## Important

This program is solely for educational purposes. Please **do not** share/distribute this code, or promote using offline version of the site in any manner. www.learncpp.com does not give permission to do so, as stated:

> Is there a PDF version of this site available for offline viewing?
>
> Unfortunately, there is not. The site is able to stay free for everyone because we’re ad-sponsored -- that model simply doesn’t work in > PDF format. You are welcome to convert pages from this website into PDF (or any other) format for your own private use, so long as you > do not distribute them.

You may test it for yourself, modify or use any part of the code in your own scripts.

## Installation 

### Windows

You should have Python 3 and the Python launcher installed on your system. 

```
git clone https://github.com/lollichop/www.learncpp.com-Crawler.git
cd www.learncpp.cm-Crawler
```
###### If multiple versions of Python is installed, use: `py -3.6 main.py [args]`
###### Otherwise, `python main.py [args]`

### Linux

You should have Python 3 installed on your system.

```
git clone https://github.com/lollichop/www.learncpp.com-Crawler.git
cd www.learncpp.cm-Crawler
python3 main.py [args]
```

## Usage

```
main.py [-h] [-o OUTPUT] [--nopdf]

optional arguments:
  -h, --help                    show this help message and exit
  -o OUTPUT, --output OUTPUT    download location
  --nopdf                       save the webpages as html
 ```
