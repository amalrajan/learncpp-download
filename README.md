# www.learncpp.com Website Crawler

[![Build Status](https://travis-ci.org/amalrajan/learncpp-download.svg?branch=master)](https://travis-ci.org/amalrajan/learncpp-download)
[![codecov](https://codecov.io/gh/amalrajan/learncpp-download/branch/master/graph/badge.svg)](https://codecov.io/gh/amalrajan/learncpp-download)


_The primary aim is demonstrate how to fetch tutorials from www.learncpp.com and store them in PDF format for offline viewing using Python._

## Important

This program is solely for educational purposes. Please **do not** share/distribute this code, or promote using offline version of the site in any manner. www.learncpp.com does not give permission to do so, as stated:

> Is there a PDF version of this site available for offline viewing?
>
> Unfortunately, there is not. The site is able to stay free for everyone because we’re ad-sponsored -- that model simply doesn’t work in > PDF format. You are welcome to convert pages from this website into PDF (or any other) format for your own private use, so long as you > do not distribute them.

You may test it for yourself, modify or use ~any part of the code in your own scripts~.

## Support www.learncpp.com

_Visit https://www.learncpp.com/about/#Support_

> LearnCpp.com is a totally free website devoted to teaching you to program in C++. Whether you’ve had any prior experience programming or not, the tutorials on this site will walk you through all the steps you’ll need to know in order to create and compile your programs. Becoming an expert programmer won’t happen overnight, but with a little patience, you’ll get there. And LearnCpp.com will show you the way.
>
> Did we mention the site is completely free? And not free as in “First one is free, man!”, nor “This wonderful synopsis of our content is completely free. Full access for 3 months is only $129.99!”. LearnCpp.com is totally, 100% free, no strings, no catches, no hidden fees, no taxes, and no license and documentation charges.
>
> So, the obvious question is, “what’s in it for us?”. Two things:
>
> We love to teach, and we love to talk about programming. This site allows us to do that without having to get a PhD, grade homework, and deal with students who need to have the final moved because their “cat just died” (sorry kitty!). Furthermore, our readers are creative, inventive, and very intelligent -- sometimes they teach us stuff in return! So we learn while we teach you, and that makes us better in our careers or hobbies. Plus, it allows us to give something back to the internet community at large. We’re just trying to make the world a better place, okay!?! (*sniff*)
> Advertising revenues. See those adsense ads on the right? Every time someone clicks one, we make a few cents. It’s not much, but it’s (hopefully) enough to at least pay the hosting fees and maybe buy ourselves a Hawaiian pizza and a pint of Newcastle every once in a while*.

## Installation 

### Windows

You should have Python 3 and the Python launcher installed on your system. 

#### Installing additional dependencies

Visit https://wkhtmltopdf.org/downloads.html to download and configure the package for Windows users.

#### Cloning the repository
```
git clone https://github.com/amalrajan/learncpp-download.git
cd learncpp-download
```
###### If multiple versions of Python is installed, use: `py -3.6 main.py [args]`
###### Otherwise, `python main.py [args]`

### Linux

You should have Python 3 installed on your system.

#### Installing additional dependencies

```
sudo apt install wkhtmltopdf
```

#### Cloning the repository

```
git clone https://github.com/amalrajan/learncpp-download.git
cd learncpp-download
python3 main.py [args]
```

## Usage

### Windows

```
py -3.6 main.py [-h] [-o OUTPUT] [--nopdf]
```

### Linux

```
python3 main.py [-h] [-o OUTPUT] [--nopdf]
```

```
optional arguments:
  -h, --help                    show this help message and exit
  -o OUTPUT, --output OUTPUT    download location
  --nopdf                       save the webpages as html
 ```
 
 #### Example usage
 
 ```
python3 main.py --output "/home/amalr/"
```
