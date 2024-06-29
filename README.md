<h1 align="center">LearnCPP Downloader</h1>

<p align="center">
  An advanced web scraper tool that seamlessly fetches and combines over 350 online tutorials into a convenient offline PDF format.
</p>

## Support ❤️

Please support here: https://www.learncpp.com/about/


## Execution


### Docker

Get the image
```bash
docker pull amalrajan/learncpp-download:latest
```

And run the container
```bash
docker run --rm --name=learncpp-download --mount type=bind,destination=/app/learncpp,source=/home/amalr/temp/downloads amalrajan/learncpp-download
```

Replace `/home/amalr/temp/downloads` with a local path on your system where you'd want the files to get downloaded.


### Local

#### Install these dependencies

1. Python 3.10.12

2. wkhtmltopdf
  - Debian based: `sudo apt install wkhtmltopdf`  
  - macOS: `brew install Caskroom/cask/wkhtmltopdf`
  - Windows: `choco install wkhtmltopdf` (or simply download it the old fashioned way). I wouldn't recommend using Windows, as the fonts are a bit weird. Unless of course, you have a thing for weird stuff.


#### Run it

Clone the repository
```bash
git clone https://github.com/amalrajan/learncpp-download.git
```

Install Python dependencies
```bash
cd learncpp-download
pip install -r requirements.txt
```

Run the script
```bash
scrapy crawl learncpp 
```

You'll find the downloaded files inside `learncpp` directory under the repository root directory.

## FAQ

#### I'm getting rate limit errors. What should I do?
Go to `settings.py` and set `DOWNLOAD_DELAY` to a higher value. The default is 0. Try setting it to 0.2.

#### Don't see what you are looking for?
Feel free to open a new issue here: https://github.com/amalrajan/learncpp-download/issues. Don't forget to attach those console logs.

## License

[The MIT License](https://choosealicense.com/licenses/mit/)
