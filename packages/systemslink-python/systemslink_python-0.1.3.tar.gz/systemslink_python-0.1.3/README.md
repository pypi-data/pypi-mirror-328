# SystemsLink Energy Manager Data Scraper

This project aims to provide a Python library capable of retrieving data from an instance of SystemsLink Energy Manager.

> ⚠️ Please note: To my knowledge, the SystemsLink energy monitoring platform does not offer any public APIs from which data can be retrieved. Instead, this system will step through the standard authentication and requests procedure as would be used by a normal user accessing the webpage.


> ⚠️ Disclaimer: This software is being developed completely independently and without endorsement form SystemsLink 2000 Ltd. It is provided free of charge and without warranty, you should feel free to use and modify it at your own risk.

## Installation
The systemslink-python project can be downloaded directly from pypi.org (https://pypi.org/project/systemslink-python/) using the pip package manager:
```bash
pip install systemslink-python
```

## What you need
- SystemsLink Server address: where you normally access your dashboard from, in my case it is of the form *xxxx.energymonitorlive.com*
- Username: Username or email address you use to login to the SystemsLink portal
- Password: Normal login password for the SystemsLink server
- Site ID: Since I only have access to a single building and meter I can't say for certain how it will look in all cases. You can find your SiteID by clicking first on 'My Site' and looking for the number in the URL bar
![A screenshot that shows where to find the Site ID in the URL bar](docs/img/siteID_url.png)

## Usage
Create an instance of the SystemsLinkAPI class:
```python
from systemslink_python import SystemsLinkAPI

my_SystemsLink = SystemsLinkAPI("https://xxxx.energymanagerlive.com/",
                                "<username>", "<password>", 96)
```

Get data from your meter:
```python
from datetime import date

# Select my_meter as the first one that is returned
my_meter = my_SystemsLink.get_meters()[0]

# Get a list of half-hourly data-points from a specific date (19th April 2024)
response_data_day = my_meter.get_amr_data(date(2024,4,19))

# Get a list of half-hourly data-points for the previous 365 days (starting
# from 19th March 2024)
response_data_year = my_meter.get_year_data(date(2024,3,19))
```

## Important: `get_year_data` vs. `get_amr_data`
It is important to know the difference between `get_year_data` and `get_amr_data`.
- `get_amr_data` makes a single request for the standard user-interface and parses 24 hours of data from the javascript contained in the response.
- `get_year_data` makes a single request and gathers an entire years worth of data by downloading the year report spreadsheet and parsing data from there. Downloaded spreadsheets are cached in case the same time-period is requested again. 

With this in mind, you should use `get_year_data` if you need data from more than a very small number of days to avoid excessive requests to your SystemsLink server.

## Caching
The `systemslink-python` library makes an attempt to cache data from the SystemsLink server. After authenticating, the server will return an auth cookie which is cached in a folder called `cache`. Since the cookie expires after only 2 hours, this may be of limited use unless you are repeatedly restarting your application. The caching behavior can be disabled when you instantiate `SystemsLinkAPI` as follows:
```python
from systemslink_python import SystemsLinkAPI

my_SystemsLink = SystemsLinkAPI("https://xxxx.energymanagerlive.com/",
                                "<username>", "<password>", 96,
                                disable_cookie_cache=True)
```
Excel reports downloaded by `get_year_data` are also stored in the `cache` directory. This behavior cannot currently be disabled.