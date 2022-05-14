import logging
import os
import sys
import time
from typing import Optional

import pdfkit
import ray
import weasyprint

from helper import scraper


class Render:
    download_path = 'downloads'

    def __init__(self, cooldown: Optional[int] = 0) -> None:
        self.urls = []
        self.cooldown = cooldown
        self.make_download_dir()

    def make_download_dir(self) -> None:
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def get_urls(self):
        return scraper.get_urls(self.cooldown)

    @staticmethod
    def get_filename(sno: int, url: str):
        return Render.download_path \
               + '/' \
               + str(sno).zfill(3) \
               + '-' \
               + url.split('/')[-2] \
               + '.pdf'

    @staticmethod
    def progress(count: int, total: int, status: Optional[str] = '') -> None:
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()


class WkRender(Render):
    options = {
        'cookie': [('ezCMPCookieConsent', '-1=1|1=1|2=1|3=1|4=1')],
        'disable-javascript': None,
        'page-size': 'A4',
        'margin-top': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'margin-right': '0'
    }

    def __init__(self) -> None:
        super().__init__()
        self.cooldown = 0
        self.urls = self.get_urls()

    def set_cooldown(self, cooldown: int) -> None:
        self.cooldown = cooldown

    def download(self) -> None:
        futures = []
        for it, url in enumerate(self.urls):
            logging.info(f'Downloading: {url}')
            futures.append(ray_download.remote(1 + it, url))
            Render.progress(it, len(self.urls))
            time.sleep(self.cooldown)

        ray.get(futures)


class WeasyRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.urls = self.get_urls()

    def download(self) -> None:
        futures = []
        for it, url in enumerate(self.urls):
            logging.info(f'Downloading: {url}')
            futures.append(ray_download_weasy.remote(1 + it, url))
            Render.progress(it, len(self.urls))
            time.sleep(self.cooldown)

        ray.get(futures)


@ray.remote
def ray_download(sno: int, url: str) -> None:
    filename = Render.get_filename(sno, url)

    try:
        pdfkit.from_url(url, filename, options=WkRender.options)
    except Exception as e:
        logging.error(f'unable to download: {url}')
        logging.exception(e)


@ray.remote
def ray_download_weasy(sno: int, url: str) -> None:
    pdf = weasyprint.HTML(url).write_pdf()
    filename = Render.get_filename(1 + sno, url)
    open(filename, 'wb').write(pdf)


logging.basicConfig(
    level=logging.WARN,
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'
)
