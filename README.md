# LearnCPP Downloader

Multi-threaded web scraper to download all the tutorials from <a href="https://www.learncpp.com/">www.learncpp.com</a> and convert them to PDF files concurrently.

## Support ❤️

Please support here: <https://www.learncpp.com/about/>

## Usage

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

You need Python 3.10 and `wkhtmltopdf` installed on your system.

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

**Rate Limit Errors:**

- Modify `settings.py`.
- Increase `DOWNLOAD_DELAY` (default: 0) to 0.2.

**High CPU Usage:**

- Adjust `max_workers` in `learncpp.py`.
- Decrease from default 192 to reduce CPU load.

```python
self.executor = ThreadPoolExecutor(
    max_workers=192
)  # Limit to 192 concurrent PDF conversions
```

**Further Issues:**

- Report at <https://github.com/amalrajan/learncpp-download/issues>. Attach console logs.

## License

[GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.en.html)
