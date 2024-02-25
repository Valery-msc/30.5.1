from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest



class TestShowMyPets:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = "qap145@og.ru"
        self.password = "123321"


    def test_login(self, driver):
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("qap145@og.ru")
        driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("123321")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Выйти')]")
        time.sleep(2)
        return 0

    def test_show_my_pets(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(self.user)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(self.password)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(5)
        assert driver.find_element(By.CSS_SELECTOR, "h1").text == "PetFriends"
        # неявное ожидание
        driver.implicitly_wait(10)
        # явное ожидание
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))
        # либо
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выйти')]")))


        images = driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-img-top'))
        names = driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-title'))
        descriptions = driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-text'))

        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ', ' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0

        return 0