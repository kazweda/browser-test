from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAdmin(object):
    def setup_method(self):
        self.driver = webdriver.Chrome()
        
    def teardown_method(self):
        self.driver.quit()

    def test_admin_title(self):
        self.driver.get("http://127.0.0.1:8000/admin")
        assert self.driver.title == "ログイン | Django サイト管理"

    def test_admin_login(self):
        self.driver.get("http://127.0.0.1:8000/admin")
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys("admin")
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys("password")
        login_button = self.driver.find_element(by=By.CSS_SELECTOR, value="input[type='submit']")
        login_button.click()
        self.driver.implicitly_wait(0.5)
        assert self.driver.title == "サイト管理 | Django サイト管理"