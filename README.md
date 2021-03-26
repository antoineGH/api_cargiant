## Null byte Scrapper

## Table of contents

-   [General info](#general-info)
-   [Screenshots](#screenshots)
-   [Technologies](#technologies)
-   [Setup](#setup)

## General info

Those projects aims to practice website data scraping using **Selenium drivers** and **Beautifulsoup4**.

Browse all articles on the main page to retrieve article information and save it to JSON.

Parsed data would be stored in databases in the following order:

-   id
-   link
-   title
-   summary
-   image
-   picture_fn
-   article_content

Selenium WebDriver helps to automates browser and fetch information with beautifulsoup4

## Screenshots

![BS4 Screenshot](https://github.com/antoineratat/null_byte_parser/blob/master/screenshots/1.PNG?raw=true)

## Technologies

Project is created with:

-   Python v3.8.5
-   astroid v2.4.2
-   beautifulsoup4 v4.9.1
-   certifi v2020.6.20
-   chardet v3.0.4
-   colorama v0.4.3
-   idna v2.10
-   isort v4.3.21
-   lazy-object-proxy v1.4.3
-   lxml v4.5.2
-   mccabe v0.6.1
-   pylint v2.5.3
-   requests v2.24.0
-   selenium v3.141.0
-   six v1.15.0
-   soupsieve v2.0.1
-   SQLAlchemy v1.3.18
-   toml v0.10.1
-   urllib3 v1.25.10
-   wrapt v1.12.1

## Setup

Install Chrome Driver for your OS : https://sites.google.com/a/chromium.org/chromedriver/home

Put the driver exe in null_byte_parser folder.

```
$ git clone https://github.com/antoineratat/null_byte_parser.git
$ py -3 -m venv venv
$ venv\Script\Activate
$ cd null_byte_parser
$ pip install -r requirements.txt
$ python run.py
```
