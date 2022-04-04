"""Utility functions for the scraper"""

from selenium.webdriver.chrome.options import Options



def parse(string: str) -> str:
    """Parse the price"""
    return (
        string.strip()
        .split()[0]
        .replace(",", ".")
        .replace("$", "")
        .replace("£", "")
        .replace("€", "")
        .replace("₹", "")
    )


def set_options() -> Options:
    """Returns a options object for the webdriver."""
    opt = Options()
    opt.binary_location = "/usr/bin/brave"
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--ignore-certificate-errors-spki-list")
    opt.add_argument("--ignore-ssl-errors")
    opt.add_experimental_option(
        "excludeSwitches", ["enable-logging", "enable-automation"]
    )
    opt.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    return opt
