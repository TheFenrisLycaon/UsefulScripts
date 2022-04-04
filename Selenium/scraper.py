"""Scraper Class"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import set_options


class Scraper:
    """Scrapper Class"""

    def __init__(self) -> None:
        """Initialize the webdriver."""
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=set_options()
        )

    def get(self):
        pass

    def quit(self) -> None:
        """Quit the webdriver."""
        self.driver.quit()
