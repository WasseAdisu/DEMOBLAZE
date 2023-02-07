import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BasePage:

    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def _find(self, by, locate) -> WebElement:
        return self._driver.find_element(by, locate)

    def _open(self):
        self._driver.get("https://www.demoblaze.com/")
        self._driver.maximize_window()
        return self._driver

    def _write(self, by, locate, content):
        self._driver.find_element(by, locate).send_keys(content)

    def _click(self, by, locate):
        self._wait_until_element_is_visible(locate)
        self._find(by, locate).click()

    def _wait_until_element_is_visible(self, locate, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(e_c.visibility_of_element_located((By.XPATH, locate)))

    def message(self, error):
        self._wait_until_element_is_visible(error)
        return self._find(By.XPATH, error).text

    def get_image_path(self, locate):
        image_div = self._find(By.CLASS_NAME, locate)
        image_path = image_div.find_element(By.TAG_NAME, "img").get_property('src')
        return image_path

    def check_product(self, errpath):
        self._wait_until_element_is_visible(errpath)
        return self._find(By.XPATH, errpath).text

    def alert_ok(self):
        sleep(1)
        self._driver.switch_to.alert.accept()

    def alert_dis(self):
        self._driver.switch_to.alert.dismiss()

    def alert_get(self):
        return self._driver.switch_to.alert.text

    def tea_dowm(self):
        return self._driver.quit()

    def is_test_display(self, by, locate):
        return self._driver.find_elements(by, locate)

