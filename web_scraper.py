import os
# 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 
from utils.sleep import sleep

if not os.path.exists(os.path.join(".", "data")):
    os.mkdir(os.path.join(".", "data"))

scraped_data : list = []

PATH_TO_CHROME_DRIVER : str = ""

WEBSITE_LINK : str = ""

DOWNLOAD_FILE_PATH : str = ""

driver : webdriver.Chrome = webdriver.Chrome(executable_path = PATH_TO_CHROME_DRIVER)
driver.get(WEBSITE_LINK)

# 

def get_by_css(css_tag : str):
    result_by_css_tag = driver.find_element(By.CSS_SELECTOR, 'div.result')
    for result in result_by_css_tag:
        info = result.find_element(By.CSS_SELECTOR, css_tag).text
        # or if it is a link
        # info = result.find_element(By.CSS_SELECTOR, css_tag).get_attribute("href")
        scraped_data.append(info)
        sleep()
    

def get_downloadable_data():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DOWNLOAD_FILE_PATH,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    new_driver = webdriver.Chrome(options=chrome_options)
    new_driver.get(WEBSITE_LINK)

    links = driver.find_elements("xpath", "//a[contains(@href, '.pdf') or contains(@href, '.csv')]")

    for link in links:
        link.click()
        sleep()

if __name__ == "__main__":
    pass