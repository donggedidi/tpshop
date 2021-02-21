from selenium import webdriver

import page
class GetDriver:

    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.URL)
            return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None

if __name__ == '__main__':
    GetDriver().get_driver()


