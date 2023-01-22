from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

s = Service('./chromedriver')

# при запуске Chrom разворачивается на полный экран
chromeOptions = Options()
chromeOptions.add_argument('start-maximized')

driver = webdriver.Chrome(service=s, options=chromeOptions)
driver.implicitly_wait(10)

driver.get('https://5ka.ru/special_offers')
wait = WebDriverWait(driver, 10)

# нажать кнопку с подтверждением выбора региона
region_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-main focus-btn location-confirm__button red']")))
region_button.click()

# нажать кнопку с подтверждением cookie
cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-main focus-btn red small']")))
cookie_button.click()

# скролинг на сайте пятерочки не включен, поэтому закомментируем
# for i in range(5):
#
#     goods = driver.find_elements(By.XPATH, "//div[@class='product-card item']")
#     actions = ActionChains(driver)
#     actions.move_to_element(goods[-1])
#     actions.perform()

# нажимаем 10 раз на кнопку "загрузить еще"
i = 0
while i < 10:

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-more-btn']")))
    next_button.click()
    i += 1

# формируем список товаров
goods = driver.find_elements(By.XPATH, "//div[@class='product-card item']")

# выводим название и цену товаров
for good in goods:
     name = good.find_element(By.XPATH, ".//div[@class='item-name']").text
     price = good.find_element(By.XPATH, ".//span[@class='from']/..").text
     print(name, price)
