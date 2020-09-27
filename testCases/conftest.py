from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
     driver = webdriver.Chrome(executable_path="C:\SeleniumEnvironment\Chrome_Latest\chromedriver.exe")
     print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Ie()

    return driver


def pytest_addoption(parser): #This will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): #This will return the browser value to set up method
    return request.config.getoption("--browser")


############## Pytest HTML report ######################################

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nitin Bangia'

#It is Hook for delete/Modify Environment info to Html report

# @pytest.mark.Optionalhook
# def pytest_metadata(metata):
#     metata.pop("Java", None)
#     metata.pop("Plugins", None)