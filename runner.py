import main_script
import driver_config
from supporing_scripts import url_builder



# runner function gets looped until all pages are not scraped
def main():
    driver = driver_config.driver
    website_input = input("Enter the link of the website: ")
    num_of_pages = 1200
    start_page = int(website_input.split("&")[-2].split("=")[1])
    scraper_result = main_script.scrape_it(driver, website_input, num_of_pages, start_page)
    while True not in scraper_result:
        if "xpath" in scraper_result:
            break
        driver.quit()
        driver = driver_config.driver
        print(f"scraped {scraper_result[1]} pages, trying to continue on page {scraper_result[1]+1}")
        # if incident happens we generate lnk of next page and restarting the scraper
        new_link = url_builder(website_input, scraper_result[1])
        first_page = scraper_result[1] + 1
        scraper_result = main_script.scrape_it(driver, new_link, num_of_pages, first_page)

    driver.quit()


if __name__ == '__main__':
    main()
