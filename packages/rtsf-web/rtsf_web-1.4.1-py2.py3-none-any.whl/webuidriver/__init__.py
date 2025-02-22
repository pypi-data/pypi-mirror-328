from .firefox.webdriver import WebDriver as Firefox  # noqa
from .firefox.firefox_profile import FirefoxProfile  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .chrome.options import Options as ChromeOptions  # noqa
from .ie.webdriver import WebDriver as Ie  # noqa
from .edge.webdriver import WebDriver as Edge  # noqa
# from .opera.webdriver import WebDriver as Opera  # opera不支持w3c标准，因此selenium 4存在问题
from .safari.webdriver import WebDriver as Safari  # noqa
from .remote.webdriver import WebDriver as Remote  # noqa

