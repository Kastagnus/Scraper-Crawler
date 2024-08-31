import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# agree to terms and condition popup window
def terms_and_conditions(driver):
    try:
        terms = driver.find_element(By.XPATH, "Path to object")
        actions = ActionChains(driver)
        actions.move_to_element(terms).perform()
        terms.click()
        return True
    except:
        return False

# receive all popups from popup dictionary and in case of popup click one of them
def handle_popups(driver, popup_list):
    handled = 0
    for selector in popup_list:
        try:
            time.sleep(2)
            popup = driver.find_element(By.XPATH, selector)
            actions = ActionChains(driver)
            actions.move_to_element(popup).perform()
            popup.click()
            print("popup clicked")
            time.sleep(2)
            handled += 1
            # Wait for the popup to close
        except:
            continue  # If popup not found, try the next selector
    if handled > 0:
        return True
    else:
        return False
