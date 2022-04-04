"""Main Script"""

from time import sleep

from scraper import Scraper


def main():
    """Main function"""
    bot = Scraper()
    sleep(5)
    bot.quit()


if __name__ == "__main__":
    main()
