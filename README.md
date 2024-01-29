<h1 align="center">LearnCPP Downloader</h1>

<p align="center">
  An advanced web scraper tool that seamlessly fetches and combines over 200 online tutorials into a convenient offline PDF format.
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

1. Python 3.10.12.

2. wkhtmltopdf
  - Debian based: `sudo apt install wkhtmltopdf`  
  - macOS: `brew install Caskroom/cask/wkhtmltopdf`
  - Windows: `choco install wkhtmltopdf` (or simply download it the old fashioned way)


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


## Facing trouble?

Feel free to open a new issue here: https://github.com/amalrajan/learncpp-download/issues. Don't forget to attach those console logs.

## License

[The MIT License](https://choosealicense.com/licenses/mit/)
