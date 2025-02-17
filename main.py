import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize WebDriver"""
        cls.driver = webdriver.Firefox()  # Change to webdriver.Firefox() if using Firefox
        cls.driver.maximize_window()
        cls.driver.get("https://vms.codemarshal.com/")  # Replace with your website URL

    def test_1_title(self):
        """Test if the webpage title is correct"""
        self.assertEqual("Visitor Management System", self.driver.title)

    def test_2_login(self):
        """Test login functionality"""
        self.driver.get("https://vms.codemarshal.com/auth/signin")  # Replace with actual login URL

        # Find username and password fields and login button
        username = self.driver.find_element(By.CSS_SELECTOR, "#email")  # Update selector if needed
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.relative")  # Update selector if needed

        # Enter credentials and submit
        username.send_keys("yeasarabir@gmail.com")
        password.send_keys("Aa2$yElhxp")
        login_button.click()

        time.sleep(3)  # Wait for the page to load

        # Check if login was successful
        #self.assertIn("Visitor Management System", self.driver.current_url)

    def test_3_title_dashboard(self):
        """Test if the webpage title is correct"""
        self.assertEqual("Visitor Management System", self.driver.title)
        
    def test_4_visitor_on_premise(self):
        self.driver.get("https://vms.codemarshal.com/visits/list?type=checkedIn")
        time.sleep(3)
        

    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
