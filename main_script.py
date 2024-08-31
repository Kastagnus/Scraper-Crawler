import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from myauto.popup_handling import handle_popups
from myauto.supporing_scripts import load_car_list, move_to_next_page, \
    click_listing, scrape_body
from myauto.data_storage_conf import append_data_to_excel
from myauto.conntections_config import is_connected, handle_connection
from path_library import path_dict

# script unites all components to crawl and scrape the desired objects
def scrape_it(driver, website, num_of_pages, starting_page):
    driver.get(website)
    popup_dict = path_dict.get("popups")
    popup_list = list(popup_dict.values())
    body_dict = path_dict.get("body")
    pagination_dict = path_dict.get("pagination")
    objects_dict = path_dict.get("objects_to_scrape")
    main_window = driver.current_window_handle
    print("page loaded")

    k = starting_page
    while k <= num_of_pages:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        print(f"Working on page number {k}...")
        posts = []
        handle_popups(driver, popup_list)
        time.sleep(random.uniform(2, 3))
        if k % 10 == 0:
            time.sleep(random.uniform(15, 25))
        if k % 30 == 0:
            time.sleep(60)
        for i in range(0, 30):
            load_attempt = load_car_list(driver, objects_dict.get("cars"), k)
            if load_attempt[0]:
                cars = load_attempt[1]
                if i < len(cars):
                    clicked = click_listing(driver, cars[i], handle_popups, is_connected, handle_connection,
                                            popup_list, i, k)
                    if clicked:
                        windows = driver.window_handles
                        for window in windows:
                            if window != main_window:
                                driver.switch_to.window(window)
                                break
                        post = scrape_body(driver, body_dict, k, i)
                        posts.append(post)
                        driver.close()
                        driver.switch_to.window(main_window)
                    else:
                        print(f"status of click is {clicked}")
                        continue

                else:
                    break

            elif load_attempt == "xpath":
                print("Caution! listing element locations might be changed")
                return False, "xpath"
            else:
                print(f"Couldn't load listings on page {k}, trying next page... ")
                break
        if len(posts) > 0:
            append_data_to_excel("myfile.xlsx", posts)
            print(f'{len(posts)} item from page number {k} loaded')
        else:
            print(f"No posts were retrieved on page {k}")
        next_page = move_to_next_page(driver, pagination_dict, handle_popups, is_connected, handle_connection, popup_list)
        if next_page[0]:
            time.sleep(random.uniform(3, 5))
            k += 1
        elif "xpath" in next_page:
            return False, "xpath"
        else:
            return False, k
    return True, k
