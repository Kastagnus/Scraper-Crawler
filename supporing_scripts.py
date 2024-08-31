from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException, \
    NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# webdriver wait until targetet span does not contain *-s anymore
class text_to_be_present_in_element_value(object):
    """ An expectation for checking if the given text is present in the specified element.
        locator, text
    """

    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            return self.text not in element_text
        except StaleElementReferenceException:
            return False

# loads all the desired listings on the webpage
def load_car_list(driver, location, k):
    try:
        car_listings = WebDriverWait(driver, 60).until(
            EC.visibility_of_all_elements_located((By.XPATH, location)))
        return True, car_listings
    except NoSuchElementException:
        return "xpath"

    except Exception as e:
        print(f"Unresolved problem {e}")
        driver.save_screenshot(f"Could't load cars page {k}")
        return False, "restart"

# clicks the listing object to enter on the object page
def click_listing(driver, listing, check_popup, connection_status, handle_connection, popup_list, listing_num, page):
    try:
        WebDriverWait(driver, 45).until(
            EC.element_to_be_clickable(listing)
        )
        actions = ActionChains(driver)
        actions.move_to_element(listing).perform()
        listing.click()
        return True
    except ElementClickInterceptedException:
        print(f"Element click intercepted on listing {listing_num}, page - {page} ")
        handle_connection(connection_status)
        popup = check_popup(driver, popup_list)
        if popup:
            try:
                WebDriverWait(driver, 45).until(
                    EC.element_to_be_clickable(listing)
                )
                actions = ActionChains(driver)
                actions.move_to_element(listing).perform()
                listing.click()
                return True
            except TimeoutException:
                handle_connection(connection_status)
                return False
            except Exception as e:
                print(f"Problem even after popup check")
                return False
        else:
            driver.save_screenshot(f"screenshot_{page}.png")
            print(f"Can not click on listing {listing_num} returning false")
            return False
    except TimeoutException:
        handle_connection(connection_status)
        return False
    except Exception as e:
        print(f"Unresolved problem {e}")
        return False

# scrapes desired data and builds a managed dictionary
def scrape_body(driver, body_dict, k, i):
    try:
        phone_btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, body_dict.get("phone_btn_xpath"))))
        actions = ActionChains(driver)
        actions.move_to_element(phone_btn).perform()
        phone_btn.click()
        WebDriverWait(driver, 40).until(text_to_be_present_in_element_value(
            (By.CSS_SELECTOR, body_dict.get("phone_location_css")),
            '*'))
        phone = driver.find_element(By.CSS_SELECTOR, body_dict.get("phone_location_css")).text
    except Exception as e:
        phone = "N/A"

    try:
        status = driver.find_element(By.CSS_SELECTOR, body_dict.get("status_css")).text
    except NoSuchElementException:
        status = "Customs not cleared"
    except:
        status = "N/A"
    try:
        price = driver.find_element(By.CSS_SELECTOR, body_dict.get("price_css")).text
    except NoSuchElementException:
        price = 'Negotiable'
    except:
        price = "N/A"
    try:
        vehicle_info = driver.find_element(By.CSS_SELECTOR, body_dict.get("vehicle_info_css")).text
        car = vehicle_info.split('\n')[0]
        year = vehicle_info.split('\n')[-1]
    except:
        driver.save_screenshot(f"{k} page - number {i}-vehicle info.png")
        print("screenshot saved!")
        car = 'N/A'
        year = 'N/A'
    try:
        user = driver.find_element(By.CSS_SELECTOR, body_dict.get("user_css")).text
    except:
        user = 'N/A'

    post = {
        "car": car,
        "year": year,
        "price": price,
        "status": status,
        "user": user,
        "phone": phone
    }

    return post

# crawls on pagination to move on next page after one has finished
def move_to_next_page(driver, location_dict, check_popup, connection_status, handle_connection, popup_list):
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        next_page = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, location_dict.get("pagination_css")))
        )
        actions = ActionChains(driver)
        actions.move_to_element(next_page).perform()
        next_page.click()
        return True, True
    except ElementClickInterceptedException:
        print("Pagination click intercepted\nchecking connections and popups..")
        handle_connection(connection_status)
        popup = check_popup(driver, popup_list)
        if popup:
            try:
                next_page = WebDriverWait(driver, 45).until(
                    EC.element_to_be_clickable(location_dict.get("pagination_css"))
                )
                actions = ActionChains(driver)
                actions.move_to_element(next_page).perform()
                next_page.click()
                return True, True
            except TimeoutException:
                handle_connection(connection_status)
                return False, False
            except Exception as e:
                print(f"Problem even after popup click at pagination")
                return False, False
        else:
            print("Can not paginate !")
            return False, False

    except TimeoutException:
        handle_connection(connection_status)
        return False, False
    except NoSuchElementException:
        print("Caution!, Pagination path might changed")
        return False, "xpath"

    except Exception as e:
        print(f"Unresolved problem with pagination {e}")
        driver.save_screenshot(f"pagination_false! page {k}")
        return False, False

#builds a new url accoding to the url structure of the website
def url_builder(url, k):
    splitted = url.split('&')
    splitted[-2] = f"page={k+1}"
    new_url = "&".join(splitted)
    return new_url
