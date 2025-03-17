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

    for address in addresses:
        print(f'crawl address {address}')
        driver.get(address)
        body = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        body.send_keys(Keys.END)
        time.sleep(30)
        body.send_keys(Keys.HOME)
        # first_link = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        # first_link.click()
        body = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        body.send_keys(Keys.END)
        time.sleep(30)
        body.send_keys(Keys.HOME)
        time.sleep(30)

addresses = [
    'https://javidaan.com/',
    'https://javidaan.com/pricing/',
    'https://javidaan.com/category/blog/',
    'https://javidaan.com/privacy-policy/',
    'https://javidaan.com/about/',
    'https://javidaan.com/contact/'
]

print(addresses)

trafficy(addresses)