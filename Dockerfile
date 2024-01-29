FROM ubuntu:jammy

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN set -ex \
    && apt-get -y update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
    python3 python3-pip wkhtmltopdf \
    && pip3 install -r requirements.txt

RUN mkdir -p /run/user/1000 && chown -R 0:0 /run/user/1000
RUN chmod 0700 /run/user/1000

CMD ["sh", "-c", "export XDG_RUNTIME_DIR=/run/user/1000 && scrapy crawl learncpp"]
