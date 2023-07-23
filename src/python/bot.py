from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import numpy as np

# Function to create random user names
def create_random_uname():
    length = np.random.randint(6, 12)
    uname = ''.join(chr(np.random.randint(97, 123)) for _ in range(length))
    return uname

# Toggle to run the bot on a website that has AFD enabled or not
afd_enabled = True
# afd_enabled = False

chrome_options = Options()
# Add any necessary options here if needed
# chrome_options.add_argument("--headless")  # Uncomment this line if you want to run Chrome in headless mode
chromedriver_path = "/Users/username/Downloads/chrome-mac-arm64/chromedriver.app"

driver = webdriver.Chrome(options=chrome_options)

url = ''
if afd_enabled:
    url = 'https://master.d2b5jlm4an7ad3.amplifyapp.com'
else:
    url = 'https://master.d2b5jlm4an7ad3.amplifyapp.com/#/current'

# run the bot 3 times and create 3 accounts
for i in range(3):
    # open new tab after first registration
    if i > 0:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])

    driver.get(url)
    uname = create_random_uname()

    user = driver.find_element(By.ID, 'basic_username')
    user.send_keys(uname)
    time.sleep(1)

    pw = driver.find_element(By.ID, 'basic_password')
    pw.send_keys('user123')
    time.sleep(1)

    email = driver.find_element(By.ID, 'basic_email')
    email.send_keys(uname + '@example.com')
    s = max(0.5, np.random.normal(2, 0.5))
    time.sleep(s)

    xpath = ''
    if afd_enabled:
        xpath = '/html/body/div/section/main/div/div/div[2]/div/form/div[4]/div/div/div/button'
    else:
        xpath = '/html/body/div/section/main/div/div/div/div/form/div[4]/div/div/div/button'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(60)

driver.quit()