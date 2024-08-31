from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# driver configurations
driver_path = 'C:\\Users\\ucha9\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
driver = webdriver.Chrome(service=service, options=options)

