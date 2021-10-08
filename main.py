from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.keys import Keys    
from colorama import *
import pyautogui
import undetected_chromedriver as uc
import time
init()
email = ""
password = ""
print(f'''{Fore.RED}
 _   _                     ___  ________  ______    _ _                        
| \ | |                    |  \/  /  __ \ |  ___|  | | |                       
|  \| | __ _ _ __ ___   ___| .  . | /  \/ | |_ ___ | | | _____      _____ _ __ 
| . ` |/ _` | '_ ` _ \ / _ \ |\/| | |     |  _/ _ \| | |/ _ \ \ /\ / / _ \ '__|
| |\  | (_| | | | | | |  __/ |  | | \__/\ | || (_) | | | (_) \ V  V /  __/ |   
\_| \_/\__,_|_| |_| |_|\___\_|  |_/\____/ \_| \___/|_|_|\___/ \_/\_/ \___|_|  
{Fore.CYAN}
Created By RandomBackpack.  {Fore.RESET}                                                                        
''')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

driver = uc.Chrome(desired_capabilities=caps)
driver.get("http://www.namemc.com")

# Sign-In
WebDriverWait(driver, timeout=10).until(
    ec.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/nav/ul[3]/li[1]/a'))
)

element = driver.find_element_by_xpath('//*[@id="header"]/div[2]/nav/ul[3]/li[1]/a')
element.click()

WebDriverWait(driver, timeout=10).until(
    ec.visibility_of_element_located((By.ID, 'email'))
)
element = driver.find_element_by_id('email')
element.send_keys(email)

WebDriverWait(driver, timeout=10).until(
    ec.visibility_of_element_located((By.ID, 'password'))
)
element = driver.find_element_by_id('password')
element.send_keys(password)

WebDriverWait(driver, timeout=10).until(
    ec.visibility_of_element_located((By.XPATH, '/html/body/main/div/div/div/div/div[2]/form/div/button'))
)
element = driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[2]/form/div/button')
element.click()

#Start Following
with open("names.txt", "r") as f: #Gets All Names To Follow
    for line in f:
        driver.get(f"https://namemc.com/{line.strip()}/")
        WebDriverWait(driver, timeout=10).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[3]/div/div[1]/h1'))
        )
        if check_exists_by_xpath('//*[@id="followMenuButton"]'):
            element = driver.find_element_by_xpath('//*[@id="followMenuButton"]')
            element.click()
            time.sleep(0.5)
            element = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div[2]/div/div/form/div/div/button[1]')
            element.click()
        else:
            pass
        
        
