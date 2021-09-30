import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\chromedriver.exe")
        print("chrome launching")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r"C:\\Users\sroy3\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe")
        driver.implicitly_wait(2)
    else:
        driver = webdriver.Chrome("C:\\chromedriver.exe")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


###############pytest HTML report############


#It is hook for Adding Environment info to HTML reports

def pytest_configure(config):
    config._metadata["Project Name"] = 'nop Commerce'
    config._metadata["Module name"] ='Customers'
    config._metadata["Tester"] ='Sandhya'

    #It is hook for delete/modify Environment info to HTML report
@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
