import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestStackoverflow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def test_searchbar(self):
        driver = self.driver
        driver.get("https://stackoverflow.com/")
        self.assertIn("Stack Overflow", driver.title)
        searchbar = driver.find_element(By.NAME, "q")
        searchbar.send_keys("pointers")
        searchbar.send_keys(Keys.RETURN)
        assert "We couldn't find anything" not in driver.page_source

    def test_signup_form(self):
        driver = self.driver
        driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        self.assertIn("Join the Stack Overflow community", driver.page_source)
        name = driver.find_element(By.NAME, 'display-name')
        name.send_keys("Programmer")
        email = driver.find_element(By.NAME, "email")
        email.send_keys("programmer@gmail.com")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("notaverygoodpassword")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
