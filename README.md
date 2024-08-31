MyAuto Web Scraper
Description
The MyAuto Web Scraper is a Python-based tool designed to extract detailed car listing information from myauto.ge. It captures data points such as car make, model, year, price, customs status, owner name and phone number automating the collection of large datasets for market analysis and machine learning purposes.

Features
Data Extraction: Scrapes car details including make, model, year, price, customs status, owner name and phone number
Pagination Handling: Automatically navigates through multiple pages of listings.
Robust Error Handling: Gracefully handles and logs errors and interruptions.
Output Formats: Supports saving data in  JSON format
Prerequisites
Before you can run this scraper, you need:

Python 3.7 or higher.
Selenium WebDriver.
ChromeDriver (matching your Chrome browser version).
Installation
Follow these steps to set up the scraper on your local machine:
git clone https://github.com/kastagnus/scraper-crawler.git
cd scraper
pip install -r requirements.txt

Configuration:
configure path_library.py to point all the objects to click or interact with
configure driver_config.py to build up a driver with your local webdriver
configure data_storae_conf.py to record listings on desired sheet, (create excel file in scraper directory first)
provide max number of pages to be scraped in runner.py num_of_pages

Run:
Run the runner.py
prive link of the page where lsitings are located 
wish you luck....

Contact Info:
ucha95@gmail.com
