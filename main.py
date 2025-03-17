import random

import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc
import  time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# creating chrome options

chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36")

def trafficy(addresses:list):
    driver = uc.Chrome(options=chrome_options,driver_executable_path='./chromedriver')

    while addresses:
        index = random.randint(0, len(addresses)-1)
        address = addresses.pop(index)
        driver.get(address)
        print(f'crawl address {address}')
        body = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        body.send_keys(Keys.END)
        time.sleep(30)
        body.send_keys(Keys.HOME)

addresses = [
    'http://golhaco.ir/',
    'https://golhaco.ir/shop/',
    'https://golhaco.ir/news/',
    'https://golhaco.ir/blog/',
    'https://golhaco.ir/recipe/dessert/',
    'https://golhaco.ir/recipe/main-course/',
    'https://golhaco.ir/recipe/appetizer/',
    'https://golhaco.ir/food-decorations/',
    'https://golhaco.ir/best-spices/',
    'https://golhaco.ir/food-health/',
    'https://golhaco.ir/info/',
    'https://golhaco.ir/food-culture/',
    'https://golhaco.ir/shirini-nokhodchi-recipe/',
    'https://golhaco.ir/%d8%a7%d8%aa%d8%b5%d8%a7%d9%84-%da%af%d9%84%d9%87%d8%a7-%d8%a8%d9%87-%d8%af%db%8c%d8%ac%db%8c-%d9%be%db%8c/',
    'https://golhaco.ir/production-of-brown-sugar/',
    'https://golhaco.ir/production-of-basil-seed-and-flixweed/',
    'https://golhaco.ir/originality-and-antiquity-of-the-golha-brand/',
    'https://golhaco.ir/golha-record-holder-of-certificates-and-standards/',
    'https://golhaco.ir/awarding-economy-resistane-badge/',
    'https://golhaco.ir/organic-products/',
    'https://golhaco.ir/soybeans-in-the-oil-offset-list/',
    'https://golhaco.ir/sugar-free-jelly-powder-launched/',
    'https://golhaco.ir/parts-of-entrepreneurship/',
    'https://golhaco.ir/sabzi-polo-ba-mahi/',
    'https://golhaco.ir/shirini-nokhodchi-recipe/',
    'https://golhaco.ir/halim-recipe/',
    'https://golhaco.ir/tumeric-for-skin/',
    'https://golhaco.ir/pofaki-gerdoyi-recipe/',
    'https://golhaco.ir/reshte-polo-with-chicken-recipe/',
    'https://golhaco.ir/tarkhine-ash-recipe/',
    'https://golhaco.ir/masala-spice/',
    'https://golhaco.ir/black-pepper-tea/',
    'https://golhaco.ir/best-spice-for-pizza/',
    'https://golhaco.ir/havij-gerdoo-cake-recipe/',
    'https://golhaco.ir/salad-kalam-recipe/'
]


print(addresses)

trafficy(addresses)