import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():

    service = Service(executable_path="C:/Users/SHIVA/OneDrive/Desktop/Test Automation/First_project_on_text_automation/chromedriver-win64/chromedriver.exe")
    options = webdriver.ChromeOptions()

    options.add_argument("use-fake-ui-for-media-stream")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@pytest.fixture()
def browser(request):
#def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")




