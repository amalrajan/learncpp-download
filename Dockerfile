FROM ubuntu:jammy

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN set -ex \
    && apt-get -y update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    python3 python3-pip wkhtmltopdf \
    && pip3 install -r requirements.txt

CMD ["scrapy", "crawl",  "learncpp"]
