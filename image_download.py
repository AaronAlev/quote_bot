from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from crop_img import crop
import time

def get_new_quote():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get("https://inspirobot.me/")

    generate_button = driver.find_element(By.CLASS_NAME, "btn-text")

    generate_button.click()
    time.sleep(3)

    img = driver.find_element(By.CLASS_NAME, "generated-image")
    img_src = img.get_attribute("src")
    driver.get(img_src)

    driver.save_screenshot("quote.png")

    driver.close()
    crop()

get_new_quote()