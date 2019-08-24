# RSPCA Adopt a Pet scraper

Scrapes Australia's RSPCA Adopt a Pet site for pets using the [scrapy/scrapy](https://github.com/scrapy/scrapy) framework.

## Setup

This project makes use of [pypa/pipenv](https://github.com/pypa/pipenv). Install
pipenv, navigate into the source folder, and run the following commands to get
dependencies installed.

```sh
pipenv install
pipenv shell
```

You can list scrapers by running

```sh
cd adoptapet
scrapy list
```

And run one of those scrapers with

```sh
scrapy call cats
```

## Deploy

Run the below command after authenticating with Scraping Hub

```sh
shub deploy
```
